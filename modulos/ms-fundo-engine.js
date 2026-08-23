
/* ─── fundo morph pontilhado · núcleo ────────────────────────────────────────
   Preset "linha MS" (20/08/2026): serigrafia + paralaxe, contraste 0.65.
   Entrada em diagonal, ao estilo da vitrine, introduz a primeira peça.
   API: MSFundo.montar(canvas, imagens, opcoes?) → {entrada(), pausar(v), cor(o)}
   opcoes: {ink, paper, acc, scale, prep:false, sortear:true}.
   prep:false pula a auto-exposição em JS — use com imagem já corrigida no
   arquivo, que é o que permite carrossel de oito a dez peças sem travar.
   sortear embaralha a ordem na carga. cor() troca a paleta com interpolação. */
window.MSFundo=(function(){
const VS=`#version 300 es
void main(){
  vec2 p = vec2(gl_VertexID==1 ? 3.0 : -1.0, gl_VertexID==2 ? 3.0 : -1.0);
  gl_Position = vec4(p,0.0,1.0);
}`;
const FS=`#version 300 es
precision highp float;
out vec4 frag;
uniform sampler2D uA,uB;
uniform vec2 uRes,uSA,uSB,uM;
uniform float uT,uTime,uAmp,uEdge,uDot,uAng,uAng2,uContrast,uGamma,uMode,uTrans,
              uGrain,uZoom,uAcc,uVig,uBleed,uFit,uCur,uMAmt,uMRad,uEnter;
uniform vec3 uInk,uPaper,uAccent;

float hash(vec2 p){p=fract(p*vec2(127.1,311.7));p+=dot(p,p+34.5);return fract(p.x*p.y*95.43);}
float vnoise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.0-2.0*f);
  return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}
float fbm(vec2 p){float s=0.0,a=0.5;for(int i=0;i<5;i++){s+=a*vnoise(p);p*=2.03;a*=0.5;}return s;}
mat2 rot(float a){return mat2(cos(a),-sin(a),sin(a),cos(a));}
float bayer(vec2 p){
  int x=int(mod(p.x,8.0)),y=int(mod(p.y,8.0));
  int m[64]=int[64](0,32,8,40,2,34,10,42,48,16,56,24,50,18,58,26,12,44,4,36,14,46,6,38,
    60,28,52,20,62,30,54,22,3,35,11,43,1,33,9,41,51,19,59,27,49,17,57,25,15,47,7,39,13,45,5,37,
    63,31,55,23,61,29,53,21);
  return (float(m[y*8+x])+0.5)/64.0;
}
// enquadra (contain ou sangria) e devolve luminância; uBleed vira linha em massa tonal
float lum(sampler2D t, vec2 imgSize, vec2 uv){
  float ca=uRes.x/uRes.y, ia=imgSize.x/imgSize.y;
  vec2 sc = uFit>0.5 ? (ca>ia ? vec2(1.0,ca/ia) : vec2(ia/ca,1.0))
                     : (ca>ia ? vec2(ia/ca,1.0) : vec2(1.0,ca/ia));
  vec2 q=(uv-0.5)/(sc*(uFit>0.5?1.0:0.86))+0.5;
  if(q.x<-0.05||q.x>1.05||q.y<-0.05||q.y>1.05) return 1.0;
  vec2 qq=vec2(clamp(q.x,0.0,1.0),1.0-clamp(q.y,0.0,1.0));
  vec4 c=mix(texture(t,qq),textureLod(t,qq,2.0+uBleed*4.5),uBleed);
  float l=mix(1.0, dot(c.rgb,vec3(0.299,0.587,0.114)), c.a);
  if(q.x<0.0||q.x>1.0||q.y<0.0||q.y>1.0) l=mix(1.0,l,uBleed*0.6);
  return l;
}
float cover(vec2 q,float cell,float r){          // cobertura de um ponto da trama
  vec2 g=mod(q,cell)-cell*0.5;
  return 1.0-smoothstep(-0.9,0.9,length(g)-r);
}

void main(){
  vec2 uv=gl_FragCoord.xy/uRes;
  float br=sin(uTime*0.18)*0.5+0.5;
  uv=(uv-0.5)*(1.0-uZoom*br)+0.5+vec2(sin(uTime*0.07),cos(uTime*0.05))*uZoom*0.35;

  // ---- cursor ---------------------------------------------------------------
  float asp=uRes.x/uRes.y;
  vec2 mp=uM/uRes;
  vec2 dm=(uv-mp)*vec2(asp,1.0);
  float rr=length(dm)/(max(uMRad,1.0)/uRes.y);
  float fm=exp(-rr*rr*2.0)*uMAmt;
  float cellMod=1.0, angMod=0.0, glitch=0.0, light=1.0, sharp=0.0;
  vec2 pxA=vec2(0.0), pxB=vec2(0.0);
  if(uCur>0.5&&uCur<1.5){                                   // foco: resolve onde se olha
    cellMod=1.0-fm*0.45; sharp=fm*0.30;
  }else if(uCur>1.5&&uCur<2.5){                             // luz: claridade rasante
    float ring=exp(-pow(rr-1.35,2.0)*3.0)*uMAmt;
    light=1.0-fm*0.55+ring*0.20;
  }else if(uCur>2.5&&uCur<3.5){                             // paralaxe: as duas camadas
    /* as amplitudes trocam de papel ao longo da passagem: a que entra com 0.026
       termina em 0.012, que é exatamente o valor com que reaparece como camada A
       no ciclo seguinte. Sem isso há um salto a cada troca de peça.            */
    vec2 d=(mp-0.5)*uMAmt;
    pxA=d*mix(0.012,0.026,uT); pxB=d*mix(0.026,0.012,uT);
  }else if(uCur>3.5&&uCur<4.5){                             // ímã: a trama abre
    cellMod=1.0+fm*1.8; angMod=fm*30.0;
  }else if(uCur>4.5){                                       // quebra: fenda fina
    float t2=floor(uTime*7.0);
    float w2=(1.5+9.0*uMAmt)/uRes.x;
    float band=step(abs(uv.x-mp.x),w2);
    uv.y+=band*(hash(vec2(t2,7.0))-0.5)*0.10*uMAmt;
    float rowH=0.030;
    float row=floor((uv.y-mp.y)/rowH);
    float h=hash(vec2(row,t2));
    float tear=step(0.55,h)*step(abs(uv.y-mp.y),rowH*1.6)*step(abs(uv.x-mp.x),0.06+0.10*uMAmt);
    uv.x+=(h-0.5)*0.045*uMAmt*tear;
    glitch=max(band,tear*0.55);
    cellMod=1.0+band*0.6*uMAmt;
  }

  // ---- luminâncias das duas peças ------------------------------------------
  float t=uT;
  vec2 n=vec2(fbm(uv*2.6+uTime*0.03), fbm(uv*2.6+7.3-uTime*0.025))*2.0-1.0;
  float bump=sin(t*3.14159);
  vec2 dA=uv+pxA, dB=uv+pxB;
  if(uTrans<0.5){ dA+=n*uAmp*t*bump; dB-=n*uAmp*(1.0-t)*bump; }
  float a=clamp((lum(uA,uSA,dA)-0.5)*(uContrast+sharp)+0.5,0.0,1.0);
  float b=clamp((lum(uB,uSB,dB)-0.5)*(uContrast+sharp)+0.5,0.0,1.0);
  float vA=pow(1.0-a,uGamma), vB=pow(1.0-b,uGamma);

  // frente que varre da esquerda para a direita
  float soft=0.06+uEdge*0.55;
  float front=mix(-soft,1.0+soft,t);
  float w=clamp((front-uv.x+soft)/(2.0*soft),0.0,1.0);

  float cell=max(uDot*cellMod,2.0);
  vec2 p=gl_FragCoord.xy-0.5*uRes;
  vec2 q=rot(radians(uAng+angMod))*p;
  float v=0.0, ink=0.0, band=0.0;

  if(uTrans<0.5){                                  // morph — dissolução por ruído
    float th=mix(fbm(uv*7.5+31.7),vnoise(uv*uRes.x/26.0),0.35);
    float e=clamp(uEdge,0.02,1.0);
    float lo=th*(1.0-e);
    float k=smoothstep(lo,lo+e,t);
    v=mix(vA,vB,k);
    band=smoothstep(0.42,0.5,k)*(1.0-smoothstep(0.5,0.58,k));
  }else if(uTrans<1.5){                            // entrelaço — cada ponto escolhe um lado
    float own=step(hash(floor(q/cell)+0.5),w);
    v=mix(vA,vB,own);
    band=exp(-pow((uv.x-front)/(soft*0.8),2.0)*2.0);
  }else if(uTrans<2.5){                            // serigrafia — duas telas, dois ângulos
    vec2 qB=rot(radians(uAng+angMod+uAng2))*p;
    float iA=cover(q ,cell,sqrt(max(vA*(1.0-w),0.0))*cell*0.70)*smoothstep(0.0,0.02,vA*(1.0-w));
    float iB=cover(qB,cell,sqrt(max(vB*w      ,0.0))*cell*0.70)*smoothstep(0.0,0.02,vB*w);
    ink=1.0-(1.0-iA)*(1.0-iB);
    v=vA*(1.0-w)+vB*w;
    band=exp(-pow((uv.x-front)/(soft*0.8),2.0)*2.0);
  }else{                                           // maré — a massa do desenho conduz
    float th=mix(uv.x,1.0-vA,0.42);
    float k=smoothstep(th-soft,th+soft,front);
    v=mix(vA,vB,k);
    v*=1.0-0.30*exp(-pow((front-th)/soft,2.0)*2.0);
    band=exp(-pow((front-th)/soft,2.0)*2.0);
  }
  v*=light;

  if(uTrans>1.5&&uTrans<2.5){                      // serigrafia já montou a tinta
  }else if(uMode<0.5){ ink=cover(q,cell,sqrt(max(v,0.0))*cell*0.70); }
  else if(uMode<1.5){ ink=1.0-smoothstep(-0.8,0.8,abs(mod(q.y,cell)-cell*0.5)-v*cell*0.5); }
  else if(uMode<2.5){ ink=step(bayer(gl_FragCoord.xy/max(1.0,cell/6.0)),v); }
  else { ink=v; }
  ink*=smoothstep(0.0,0.05,v);

  /* ---- entrada diagonal: a trama nasce ao longo de uma reta inclinada ---- */
  float sx=uv.x+(uv.y-0.5)*0.26;                 // eixo da varredura, ~14° de inclinação
  float bandW=0.30;
  float fEnter=uEnter*(1.0+2.0*bandW)-bandW;
  float rev=clamp((fEnter-sx)/bandW+0.5,0.0,1.0);
  float fio=exp(-pow((sx-fEnter)/0.0045,2.0))*step(0.001,uEnter)*step(uEnter,0.999);
  ink*=rev; band=mix(band,0.0,1.0-rev);

  vec3 tinta=mix(uInk,uAccent,clamp(band,0.0,1.0)*uAcc);
  vec3 col=mix(uPaper,tinta,clamp(ink,0.0,1.0));
  col=mix(col,uAccent,clamp(fio,0.0,1.0)*0.85);
  col=mix(col,uAccent,glitch*0.12*uMAmt);
  col+= (hash(gl_FragCoord.xy+fract(uTime)*97.0)-0.5)*uGrain;
  float d=length((uv-0.5)*vec2(asp,1.0));
  col=mix(col,uPaper*0.96+uInk*0.04,smoothstep(0.42,0.95,d)*uVig);
  frag=vec4(col,1.0);
}`;

function montar(cv, IMGS, OPT){
  OPT = OPT || {};
  const gl=cv.getContext('webgl2',{antialias:false,powerPreference:'low-power'});
  if(!gl) return {entrada(){},pausar(){}};
  function sh(t,src){const s=gl.createShader(t);gl.shaderSource(s,src);gl.compileShader(s);
    if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))console.error(gl.getShaderInfoLog(s));return s;}
  const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,VS));
  gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,FS));gl.linkProgram(pr);
  if(!gl.getProgramParameter(pr,gl.LINK_STATUS))console.error(gl.getProgramInfoLog(pr));
  gl.useProgram(pr);gl.bindVertexArray(gl.createVertexArray());
  const U={};for(const k of ['uA','uB','uRes','uSA','uSB','uM','uT','uTime','uAmp','uEdge','uDot',
   'uAng','uAng2','uContrast','uGamma','uMode','uTrans','uEnter','uGrain','uZoom','uAcc','uVig',
   'uBleed','uFit','uCur','uMAmt','uMRad','uInk','uPaper','uAccent'])U[k]=gl.getUniformLocation(pr,k);
  gl.uniform1i(U.uA,0);gl.uniform1i(U.uB,1);
  const P={trans:2,cur:3,mode:0,fit:1,dot:4.5,angle:22,angle2:32,bleed:.42,contrast:.65,
    gamma:1.45,amp:.08,edge:1.0,speed:.30,zoom:.01,accent:0,grain:0,vig:.86,mforce:.46,mrad:240};
  const hex=h=>[1,3,5].map(i=>parseInt(h.substr(i,2),16)/255);
  const INK=hex(OPT.ink||'#0e0f0b'),PAPER=hex(OPT.paper||'#6B6A4B'),
        ACC=hex(OPT.acc||'#B85C38'),SCALE=OPT.scale||0.9;
  /* paleta trocável em tempo real: MSFundo.montar(...).cor({paper:'#B85C38'}) */
  const COR={ink:INK.slice(),paper:PAPER.slice(),acc:ACC.slice()};
  const ALVO={ink:INK.slice(),paper:PAPER.slice(),acc:ACC.slice()};
  function prep(src){
    if(OPT.prep===false) return src;   // já pré-exposta no arquivo
    const w=src.naturalWidth,h=src.naturalHeight;
    const c=document.createElement('canvas');c.width=w;c.height=h;
    const x=c.getContext('2d',{willReadFrequently:true});x.drawImage(src,0,0);
    let d;try{d=x.getImageData(0,0,w,h);}catch(e){return src;}
    const a=d.data;let s=0,n=0;
    for(let k=0;k<a.length;k+=64){s+=(a[k]*.299+a[k+1]*.587+a[k+2]*.114)/255;n++;}
    const mean=s/Math.max(n,1); if(mean>=0.45) return src;
    const g=Math.max(0.42,Math.log(0.50)/Math.log(Math.max(mean,0.03)));
    const lut=new Uint8Array(256);for(let v=0;v<256;v++)lut[v]=Math.round(255*Math.pow(v/255,g));
    for(let k=0;k<a.length;k+=4){a[k]=lut[a[k]];a[k+1]=lut[a[k+1]];a[k+2]=lut[a[k+2]];}
    x.putImageData(d,0,0);return c;
  }
  function mkTex(raw){
    const src=prep(raw);const t=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,t);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR_MIPMAP_LINEAR);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);
    gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,src);
    gl.generateMipmap(gl.TEXTURE_2D);
    return {tex:t,w:src.width||src.naturalWidth,h:src.height||src.naturalHeight};
  }
  let S=[],i=0,t=0,clock=0,last=performance.now(),ready=false,visible=true,paused=false;
  let mx=0,my=0,tmx=0,tmy=0,mAmt=0,mOn=false,enter=1,enterT=0;
  const easeOut=x=>1-Math.pow(1-x,3);
  function resize(){const d=Math.min(devicePixelRatio||1,2)*SCALE;
    cv.width=Math.round(cv.clientWidth*d)||Math.round(innerWidth*d);
    cv.height=Math.round(cv.clientHeight*d)||Math.round(innerHeight*d);
    gl.viewport(0,0,cv.width,cv.height);}
  addEventListener('resize',resize);resize();
  addEventListener('pointermove',e=>{const k=cv.width/(cv.clientWidth||innerWidth);
    tmx=e.clientX*k;tmy=cv.height-e.clientY*k;
    if(mAmt<0.02){mx=tmx;my=tmy;}mOn=true;});
  addEventListener('pointerleave',()=>mOn=false);
  document.addEventListener('visibilitychange',()=>visible=!document.hidden);
  if('IntersectionObserver' in window)
    new IntersectionObserver(e=>{visible=e[0].isIntersecting&&!document.hidden;},{threshold:.01}).observe(cv);
  if(matchMedia('(prefers-reduced-motion: reduce)').matches) paused=true;
  let FILA=IMGS.slice();
  if(OPT.sortear){ for(let j=FILA.length-1;j>0;j--){
    const r=Math.floor(Math.random()*(j+1)); const t=FILA[j]; FILA[j]=FILA[r]; FILA[r]=t; } }
  (async()=>{ for(const src of FILA){
    const im=await new Promise(r=>{const x=new Image();x.onload=()=>r(x);x.onerror=()=>r(null);x.src=src;});
    if(im) S.push(mkTex(im)); if(S.length===2) ready=true;
    await new Promise(r=>setTimeout(r,0));
  } if(S.length) ready=true; })();
  function frame(now){
    requestAnimationFrame(frame);
    if(!visible||!ready){last=now;return;}
    const dt=Math.min((now-last)/1000,.05);last=now;
    if(!paused){clock+=dt;t+=dt*P.speed*0.5;if(t>=1){t=0;i=(i+1)%S.length;}}
    const A=S[i],B=S[(i+1)%S.length],k=cv.width/(cv.clientWidth||innerWidth);
    const kp=1-Math.exp(-dt*9.05),ka=1-Math.exp(-dt*4.35);
    mx+=(tmx-mx)*kp;my+=(tmy-my)*kp;mAmt+=((mOn?1:0)-mAmt)*ka;
    if(enter<1){enterT+=dt;enter=Math.min(1,easeOut(Math.max(0,enterT-0.15)/1.45));}
    const kc=1-Math.exp(-dt*3.2);
    for(const nome of ['ink','paper','acc'])
      for(let c=0;c<3;c++) COR[nome][c]+=(ALVO[nome][c]-COR[nome][c])*kc;
    const e0=t*t*(3-2*t);
    gl.activeTexture(gl.TEXTURE0);gl.bindTexture(gl.TEXTURE_2D,A.tex);
    gl.activeTexture(gl.TEXTURE1);gl.bindTexture(gl.TEXTURE_2D,B.tex);
    gl.uniform2f(U.uRes,cv.width,cv.height);
    gl.uniform2f(U.uSA,A.w,A.h);gl.uniform2f(U.uSB,B.w,B.h);gl.uniform2f(U.uM,mx,my);
    gl.uniform1f(U.uT,Math.min(1,Math.max(0,(e0-0.5)*1.55+0.5)));
    gl.uniform1f(U.uTime,clock);gl.uniform1f(U.uEnter,enter);
    gl.uniform1f(U.uDot,P.dot*k);gl.uniform1f(U.uAng,P.angle);gl.uniform1f(U.uAng2,P.angle2);
    gl.uniform1f(U.uBleed,P.bleed);gl.uniform1f(U.uContrast,P.contrast);gl.uniform1f(U.uGamma,P.gamma);
    gl.uniform1f(U.uAmp,P.amp);gl.uniform1f(U.uEdge,P.edge);gl.uniform1f(U.uZoom,P.zoom);
    gl.uniform1f(U.uAcc,P.accent);gl.uniform1f(U.uGrain,P.grain);gl.uniform1f(U.uVig,P.vig);
    gl.uniform1f(U.uMode,P.mode);gl.uniform1f(U.uTrans,P.trans);gl.uniform1f(U.uFit,P.fit);
    gl.uniform1f(U.uCur,P.cur);gl.uniform1f(U.uMAmt,mAmt*P.mforce);gl.uniform1f(U.uMRad,P.mrad*k);
    gl.uniform3fv(U.uInk,COR.ink);gl.uniform3fv(U.uPaper,COR.paper);gl.uniform3fv(U.uAccent,COR.acc);
    gl.drawArrays(gl.TRIANGLES,0,3);
  }
  requestAnimationFrame(frame);
  return {entrada(){enter=0;enterT=0;}, pausar(v){paused=!!v;}, P:P,
    cor(o){ if(o.ink)ALVO.ink=hex(o.ink); if(o.paper)ALVO.paper=hex(o.paper);
            if(o.acc)ALVO.acc=hex(o.acc); }};
}
return {montar:montar};
})();
