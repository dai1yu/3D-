import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="智能工厂数字孪生平台",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏 Streamlit 默认边距和工具栏，让页面更接近工业数字孪生大屏
st.markdown("""
<style>
    #MainMenu, footer, header, [data-testid="stToolbar"] {visibility: hidden;}
    .stApp {background: #06121b;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0;}
</style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智能工厂数字孪生平台</title>
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#06121b;color:#d8fbff;
font-family:"Microsoft YaHei",Arial,sans-serif}
:root{--cyan:#16d9df;--blue:#168ba8;--line:rgba(26,220,230,.48);--panel:rgba(3,24,34,.82)}
#app{position:relative;width:100vw;height:100vh;min-height:680px;overflow:hidden;background:
radial-gradient(ellipse at 50% 48%,rgba(0,111,132,.23),transparent 55%),
linear-gradient(180deg,#061724 0%,#06121b 100%)}
#scene{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.topbar{position:absolute;z-index:5;left:0;right:0;top:0;height:66px;
background:linear-gradient(180deg,rgba(3,19,29,.97),rgba(3,19,29,.48));
border-bottom:1px solid rgba(31,214,224,.35);display:flex;align-items:center;justify-content:space-between;padding:0 24px}
.brand{font-size:23px;font-weight:700;letter-spacing:5px;color:#dffcff;text-shadow:0 0 15px #00d9e9}
.brand small{display:block;font-size:9px;letter-spacing:3px;color:#56b8c4;margin-top:3px;font-weight:400}
.top-actions{display:flex;align-items:center;gap:10px}
.top-btn{border:1px solid rgba(31,219,226,.55);background:rgba(0,128,145,.18);color:#9ffaff;
padding:9px 16px;cursor:pointer;letter-spacing:1px;clip-path:polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px)}
.top-btn.active,.top-btn:hover{background:rgba(0,205,210,.35);box-shadow:0 0 14px rgba(0,224,230,.28)}
.clock{font-size:12px;color:#83cbd2;margin-left:12px;min-width:145px;text-align:right}
.panel{position:absolute;z-index:3;width:265px;background:linear-gradient(135deg,rgba(3,26,37,.92),rgba(3,18,29,.77));
border:1px solid var(--line);box-shadow:0 0 20px rgba(0,207,222,.10),inset 0 0 22px rgba(0,150,170,.08);
padding:14px 14px 12px;backdrop-filter:blur(8px)}
.panel:before,.panel:after{content:"";position:absolute;width:35px;height:2px;background:var(--cyan);box-shadow:0 0 8px var(--cyan)}
.panel:before{left:-1px;top:-1px}.panel:after{right:-1px;bottom:-1px}
.left{left:18px;top:88px;bottom:128px}
.right{right:18px;top:88px;bottom:128px}
.panel-title{font-size:14px;letter-spacing:2px;color:#b8faff;border-bottom:1px solid rgba(38,211,221,.32);
padding:0 0 11px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center}
.panel-title span{font-size:10px;color:#5bcbd3;letter-spacing:1px}
.section-label{font-size:11px;color:#57c8d1;margin:13px 0 8px;display:flex;align-items:center;gap:8px}
.section-label:before{content:"";width:5px;height:5px;background:#19dce2;box-shadow:0 0 8px #19dce2}
.device{display:flex;justify-content:space-between;align-items:center;padding:9px 8px;margin:5px 0;
border:1px solid rgba(27,170,185,.18);background:rgba(12,73,86,.18);font-size:11px;color:#b8dfe3;cursor:pointer}
.device:hover,.device.selected{border-color:#14dce3;background:rgba(0,175,190,.22);color:#e1ffff}
.dot{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:7px;background:#23e7a5;box-shadow:0 0 8px #23e7a5}
.dot.warn{background:#ffba45;box-shadow:0 0 8px #ffba45}
.dot.off{background:#768a91;box-shadow:none}
.status{color:#39e9bd;font-size:10px}
.status.warn{color:#ffc15b}
.metric-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.metric{padding:10px 8px;background:rgba(10,72,86,.28);border:1px solid rgba(27,184,195,.23);min-height:67px}
.metric label{display:block;color:#6dbbc4;font-size:10px;margin-bottom:7px}
.metric strong{font-size:19px;color:#d7ffff;font-weight:500}
.metric em{font-size:9px;color:#4de0d9;font-style:normal;margin-left:3px}
.bar-row{margin:11px 0;font-size:10px;color:#8ecbd0;display:grid;grid-template-columns:58px 1fr 34px;gap:7px;align-items:center}
.bar{height:6px;background:rgba(125,190,197,.18);overflow:hidden}
.bar i{display:block;height:100%;background:linear-gradient(90deg,#087c9b,#22e6d9);box-shadow:0 0 8px #14cfd9}
.ring-wrap{display:flex;align-items:center;gap:13px;padding:8px 2px}
.ring{width:86px;height:86px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(#14d9db 0 76%,#16667a 76% 100%);position:relative}
.ring:after{content:"";position:absolute;inset:8px;background:#09202a;border-radius:50%}
.ring b{z-index:1;font-size:19px;color:#e1ffff;font-weight:500}
.ring-info{font-size:10px;color:#7fc4cb;line-height:2}
.ring-info strong{font-size:17px;color:#dfffff}
.bottom{position:absolute;z-index:4;left:18px;right:18px;bottom:16px;height:98px;display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr 1.2fr;gap:10px}
.bottom-card{border:1px solid rgba(27,208,218,.4);background:linear-gradient(135deg,rgba(3,28,39,.93),rgba(3,17,28,.78));
padding:12px 15px;position:relative;overflow:hidden}
.bottom-card:after{content:"";position:absolute;left:0;bottom:0;height:2px;width:100%;background:linear-gradient(90deg,transparent,#13dce2,transparent)}
.bottom-card label{display:block;color:#68b9c1;font-size:10px;margin-bottom:9px}
.bottom-card strong{font-size:23px;color:#d9ffff;font-weight:500}
.bottom-card small{font-size:10px;color:#44d8c9;margin-left:5px}
.bottom-card .spark{float:right;color:#1cd8d8;font-size:23px;opacity:.8}
.corner{position:absolute;z-index:2;color:rgba(52,203,214,.7);font-size:10px;letter-spacing:2px}
.c1{top:76px;left:50%;transform:translateX(-50%)}
.c2{bottom:126px;left:50%;transform:translateX(-50%)}
.modal-mask{display:none;position:absolute;z-index:10;inset:0;background:rgba(0,8,15,.68);align-items:center;justify-content:center}
.modal-mask.show{display:flex}.modal{width:min(520px,90vw);border:1px solid #16d9df;background:linear-gradient(145deg,#082b38,#061722);box-shadow:0 0 35px #087b8a;padding:18px}
.modal-head{display:flex;justify-content:space-between;align-items:center;color:#cfffff;border-bottom:1px solid rgba(22,217,223,.35);padding-bottom:12px}
.close-btn{background:transparent;color:#8ffaff;border:1px solid #168ba8;padding:5px 10px;cursor:pointer}
.modal-body{font-size:13px;line-height:2;color:#a9dce1;padding-top:12px}.modal-body button{margin:6px 8px 0 0}
.modal-body .action{border:1px solid #16d9df;background:rgba(0,160,175,.18);color:#cfffff;padding:8px 12px;cursor:pointer}
.tooltip{position:absolute;z-index:11;left:50%;top:50%;transform:translate(-50%,-50%);padding:16px 24px;
background:rgba(3,35,44,.94);border:1px solid #16d9df;box-shadow:0 0 20px #087b8a;display:none;font-size:13px}
.tooltip.show{display:block}
@media(max-width:900px){
 .panel{width:220px}.left{left:8px}.right{right:8px}
 .bottom{left:8px;right:8px;gap:5px}.bottom-card{padding:9px 7px}
 .bottom-card strong{font-size:17px}.brand{font-size:17px}
}
</style>
</head>
<body>
<div id="app">
<canvas id="scene"></canvas>
<div class="topbar">
  <div class="brand">智能工厂数字孪生平台<small>INTELLIGENT FACTORY DIGITAL TWIN PLATFORM</small></div>
  <div class="top-actions">
    <button class="top-btn active" id="autoBtn" onclick="toggleAuto()">自动监测</button>
    <button class="top-btn" onclick="openPanel('monitor')">数据监测</button>
    <button class="top-btn" onclick="openPanel('inspect')">设备巡检</button>
    <button class="top-btn" onclick="resetCameraView()">视角复位</button>
    <div class="clock" id="clock"></div>
  </div>
</div>

<div class="corner c1">FACTORY 3D VISUALIZATION　/　数字工厂场景</div>
<div class="panel left">
  <div class="panel-title">设备运行监控 <span>DEVICE MONITOR</span></div>
  <div class="section-label">生产线设备列表</div>
  <div class="device selected" onclick="selectDevice(this,'数控加工中心 A01')"><span><i class="dot"></i>数控加工中心 A01</span><b class="status">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控车床 B02')"><span><i class="dot"></i>数控车床 B02</span><b class="status">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'智能机械臂 C03')"><span><i class="dot warn"></i>智能机械臂 C03</span><b class="status warn">待机</b></div>
  <div class="device" onclick="selectDevice(this,'自动传送线 D04')"><span><i class="dot"></i>自动传送线 D04</span><b class="status">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'检测工作站 E05')"><span><i class="dot off"></i>检测工作站 E05</span><b class="status">离线</b></div>
  <div class="device" onclick="selectDevice(this,'立式加工中心 F06')"><span><i class="dot"></i>立式加工中心 F06</span><b class="status">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'高速钻攻中心 G07')"><span><i class="dot"></i>高速钻攻中心 G07</span><b class="status">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'精密铣削中心 H08')"><span><i class="dot warn"></i>精密铣削中心 H08</span><b class="status warn">待机</b></div>
  <div class="section-label">设备实时参数</div>
  <div class="metric-grid">
    <div class="metric"><label>主轴转速</label><strong id="rpm">3200</strong><em>rpm</em></div>
    <div class="metric"><label>主轴负载</label><strong id="load">68</strong><em>%</em></div>
    <div class="metric"><label>设备温度</label><strong id="temp">36.5</strong><em>℃</em></div>
    <div class="metric"><label>运行时长</label><strong>08:26</strong><em>h</em></div>
  </div>
  <div class="section-label">设备运行状态</div>
  <div class="bar-row"><span>运行时间</span><div class="bar"><i style="width:86%"></i></div><b>86%</b></div>
  <div class="bar-row"><span>加工进度</span><div class="bar"><i style="width:72%"></i></div><b>72%</b></div>
  <div class="bar-row"><span>健康指数</span><div class="bar"><i style="width:96%"></i></div><b>96%</b></div>
  <div class="section-label">视觉检测摄像头</div>
  <div class="device" id="cameraStatus"><span><i class="dot"></i>传送带工业相机 CAM-01</span><b class="status" id="camState">在线</b></div>
  <div class="metric-grid">
    <div class="metric"><label>检测状态</label><strong id="detectState" style="font-size:15px">待检测</strong></div>
    <div class="metric"><label>当前识别数</label><strong id="detectCount">0</strong><em>件</em></div>
  </div>
</div>

<div class="panel right">
  <div class="panel-title">生产数据分析 <span>DATA ANALYSIS</span></div>
  <div class="section-label">生产运行总览</div>
  <div class="ring-wrap"><div class="ring"><b>93.8%</b></div><div class="ring-info">设备综合运行率<br><strong>正常运行</strong><br>生产线状态良好</div></div>
  <div class="section-label">关键生产指标</div>
  <div class="metric-grid">
    <div class="metric"><label>今日产量</label><strong id="output">1,286</strong><em>件</em></div>
    <div class="metric"><label>合格数量</label><strong id="goodCount">1,264</strong><em>件</em></div>
    <div class="metric"><label>不良品数</label><strong id="badCount">22</strong><em>件</em></div>
    <div class="metric"><label>合格率</label><strong id="yieldRate">98.3</strong><em>%</em></div>
  </div>
  <div class="section-label">缺陷分拣统计</div><div class="metric-grid"><div class="metric"><label>缺件数量</label><strong id="missingCount">8</strong><em>件</em></div><div class="metric"><label>废品暂存区</label><strong id="rejectBinCount">0</strong><em>件</em></div></div><div class="section-label">能源消耗监测</div>
  <div class="bar-row"><span>电力</span><div class="bar"><i style="width:72%"></i></div><b>72%</b></div>
  <div class="bar-row"><span>压缩空气</span><div class="bar"><i style="width:48%"></i></div><b>48%</b></div>
  <div class="bar-row"><span>冷却液</span><div class="bar"><i style="width:35%"></i></div><b>35%</b></div>
  <div class="section-label">实时分拣记录</div><div id="sortLog" style="font-size:10px;color:#8ecbd0;line-height:2.1">等待首件进入视觉检测区…</div>
</div>

<div class="bottom">
 <div class="bottom-card"><label>当前生产任务</label><strong>加工任务 #0826</strong><span class="spark">▰</span></div>
 <div class="bottom-card"><label>设备总数 / 在线设备</label><strong>24 / 22</strong><small>台</small></div>
 <div class="bottom-card"><label>今日生产数量</label><strong id="bottomOutput">1,286</strong><small>件</small></div>
 <div class="bottom-card"><label>平均加工效率</label><strong>96.8</strong><small>%</small></div>
 <div class="bottom-card"><label>系统运行状态</label><strong style="color:#39e8b6">正常</strong><small>ALL SYSTEMS GO</small></div>
</div>
<div class="modal-mask" id="modalMask" onclick="closePanel(event)">
 <div class="modal" onclick="event.stopPropagation()">
  <div class="modal-head"><b id="modalTitle">模块详情</b><button class="close-btn" onclick="closePanel()">✕</button></div>
  <div id="modalBody" class="modal-body"></div>
 </div>
</div>
<div class="tooltip" id="toast"></div>
</div>

<script type="importmap">
{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"}}
</script>
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';

const canvas=document.querySelector('#scene');
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(innerWidth,innerHeight);
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.15;

const scene=new THREE.Scene();
scene.background=new THREE.Color(0x061722);
scene.fog=new THREE.Fog(0x061722,24,65);
const camera=new THREE.PerspectiveCamera(43,innerWidth/innerHeight,.1,150);
camera.position.set(20,17,25);
const controls=new OrbitControls(camera,renderer.domElement);
controls.target.set(1.5,1.1,1.0);
controls.enableDamping=true;
controls.enablePan=true;
controls.minDistance=12;controls.maxDistance=48;
controls.maxPolarAngle=Math.PI*.48;
const defaultCameraPosition=new THREE.Vector3(20,17,25);
window.addEventListener('reset-twin-camera',()=>{
 camera.position.copy(defaultCameraPosition);controls.target.set(0,1,0);controls.update();
});

scene.add(new THREE.HemisphereLight(0x9eefff,0x14252d,2.0));
const key=new THREE.DirectionalLight(0xffffff,2.3);
key.position.set(10,22,12);key.castShadow=true;scene.add(key);
const cyanLight=new THREE.PointLight(0x00d9e8,32,35);cyanLight.position.set(-8,7,0);scene.add(cyanLight);
const blueLight=new THREE.PointLight(0x087bff,22,30);blueLight.position.set(8,5,-8);scene.add(blueLight);

const mat=(color,metalness=.25,roughness=.55,emissive=0x000000)=>new THREE.MeshStandardMaterial({color,metalness,roughness,emissive});
const floorMat=mat(0x142d35,.25,.82);
const floor=new THREE.Mesh(new THREE.PlaneGeometry(48,36),floorMat);
floor.rotation.x=-Math.PI/2;floor.position.y=-.08;floor.receiveShadow=true;scene.add(floor);
const grid=new THREE.GridHelper(48,48,0x087e91,0x164451);grid.position.y=-.045;scene.add(grid);

function box(parent,x,y,z,w,h,d,material,cast=true){
 const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material);
 m.position.set(x,y,z);m.castShadow=cast;m.receiveShadow=true;parent.add(m);return m;
}
const dark=mat(0x182d37,.7,.35),steel=mat(0x819aa2,.75,.28),white=mat(0xc4d4d5,.35,.38);
const green=mat(0x087e69,.45,.4),glass=new THREE.MeshStandardMaterial({color:0x0a7180,metalness:.25,roughness:.16,transparent:true,opacity:.55});
const yellow=mat(0xf0aa24,.45,.4),glow=mat(0x00cbd8,.3,.25,0x006b77);

const rubberMachine=mat(0x111a20,.15,.78),machineWhite=mat(0xb9c7cb,.62,.3),
      trimMachine=mat(0x657a82,.82,.22),screenMat=mat(0x061923,.3,.18),
      screenGlow=mat(0x087b8b,.25,.18,0x075e70);
function makeMachine(x,z,label){
  const g=new THREE.Group();g.position.set(x,0,z);scene.add(g);
  box(g,0,.38,0,3.9,.72,2.95,dark);
  box(g,0,.78,0,3.65,.16,2.72,steel);
  for(const a of [-1.48,1.48])for(const b of [-1.05,1.05]){
    box(g,a,.12,b,.48,.24,.48,dark);
    const foot=new THREE.Mesh(new THREE.CylinderGeometry(.16,.19,.12,20),rubberMachine);
    foot.position.set(a,.04,b);g.add(foot);
  }
  box(g,0,2.02,0,3.48,2.35,2.48,machineWhite);
  box(g,0,3.23,0,3.58,.16,2.58,steel);
  box(g,0,.93,0,3.55,.16,2.58,dark);
  // 正面观察门与金属门框
  box(g,0,2.02,1.265,2.72,1.68,.055,glass,false);
  box(g,-1.39,2.02,1.31,.13,1.88,.13,steel);
  box(g,1.39,2.02,1.31,.13,1.88,.13,steel);
  box(g,0,2.91,1.31,2.86,.12,.13,steel);
  box(g,0,1.12,1.31,2.86,.12,.13,steel);
  box(g,0,2.02,1.35,.055,1.68,.08,dark);
  for(const a of [-.13,.13]){
    box(g,a,1.98,1.43,.045,.42,.08,trimMachine);
    const latch=new THREE.Mesh(new THREE.CylinderGeometry(.055,.055,.07,16),dark);
    latch.rotation.x=Math.PI/2;latch.position.set(a,2.02,1.48);g.add(latch);
  }
  // 加工舱内部的工作台、主轴和刀柄
  box(g,0,1.22,.42,1.95,.18,1.12,dark);
  box(g,0,1.34,.28,1.45,.10,.72,steel);
  const spindle=new THREE.Mesh(new THREE.CylinderGeometry(.22,.28,.68,28),trimMachine);
  spindle.position.set(0,2.38,-.18);g.add(spindle);
  const spindleNose=new THREE.Mesh(new THREE.CylinderGeometry(.11,.15,.26,24),dark);
  spindleNose.position.set(0,1.91,-.18);g.add(spindleNose);
  // 左侧散热格栅
  box(g,-1.79,2.0,-.28,.06,1.25,1.25,dark);
  for(let i=0;i<8;i++)box(g,-1.835,1.48+i*.145,-.28,.035,.045,1.0,steel,false);
  // 右侧电控柜、触摸屏和实体按钮
  box(g,1.92,1.95,.05,.48,2.05,2.42,dark);
  box(g,1.92,2.08,1.29,.40,.78,.055,steel);
  box(g,1.92,2.08,1.325,.32,.60,.025,screenMat,false);
  box(g,1.92,2.08,1.344,.26,.48,.012,screenGlow,false);
  for(let i=0;i<3;i++){
    const led=new THREE.Mesh(new THREE.CircleGeometry(.035,12),new THREE.MeshBasicMaterial({color:[0x19e5c0,0xffc34d,0xff5965][i]}));
    led.position.set(1.80+i*.12,1.58,1.34);g.add(led);
  }
  box(g,1.92,1.18,1.30,.32,.38,.08,dark);
  // 顶部警示灯、设备铭牌、检修格栅
  box(g,0,3.36,-.82,.58,.12,.42,dark);
  const beaconBase=new THREE.Mesh(new THREE.CylinderGeometry(.09,.09,.18,18),steel);
  beaconBase.position.set(1.25,3.43,-.75);g.add(beaconBase);
  const beacon=new THREE.Mesh(new THREE.SphereGeometry(.11,16,12),new THREE.MeshStandardMaterial({color:0x27e5a0,emissive:0x087c45}));
  beacon.position.set(1.25,3.58,-.75);g.add(beacon);
  box(g,-.95,.84,1.34,.68,.30,.045,steel,false);
  box(g,-.95,.84,1.37,.54,.12,.018,glow,false);
  for(let i=0;i<5;i++)box(g,-1.55+i*.16,.83,-1.30,.09,.22,.025,steel,false);
  g.userData.label=label;return g;
}
// 主生产线：传送带直接对接机床进料侧，机械臂位于交接工位
const machines=[
 makeMachine(7,4,'数控加工中心 A01'),
 makeMachine(7,-5,'数控车床 B02'),
 makeMachine(-7,-5,'精密检测工作站 E05'),
 makeMachine(-7,4,'立式加工中心 F06'),
 makeMachine(0,-10.5,'高速钻攻中心 G07'),
 makeMachine(8,-10.5,'精密铣削中心 H08')
];

// 加长并前移的传送带：机床模型、位置、尺寸和朝向保持不变
// 原长度12.2，现长度24.4；整体向厂房前侧(+Z方向)移动2.2
const BELT_X=-1.1;
const BELT_Z=7.55;
const BELT_LENGTH=24.4;
const BELT_LEFT=BELT_X-BELT_LENGTH/2;
const BELT_RIGHT=BELT_X+BELT_LENGTH/2;
const beltMat=mat(0x253f49,.65,.4);
box(scene,BELT_X,.43,BELT_Z,BELT_LENGTH,.52,1.65,beltMat);
box(scene,BELT_X,.72,BELT_Z,BELT_LENGTH-.3,.08,1.35,mat(0x0a5963,.5,.3));
const beltRollers=[];
for(let i=0;i<25;i++){
 const roller=new THREE.Mesh(new THREE.CylinderGeometry(.12,.12,1.42,16),steel);
 roller.rotation.z=Math.PI/2;
 roller.position.set(BELT_LEFT+.30+i*.99,.42,BELT_Z);
 scene.add(roller);
 beltRollers.push(roller);
}
// 两侧导轨和入口导向段与传送带同步加长、前移
box(scene,BELT_X,.92,BELT_Z-.80,BELT_LENGTH-.2,.12,.10,steel);
box(scene,BELT_X,.92,BELT_Z+.80,BELT_LENGTH-.2,.12,.10,steel);
box(scene,BELT_RIGHT-.25,.78,BELT_Z,.45,.18,1.55,yellow);

// =====================================================
// 传送带最左端收纳盒：开放式工业金属周转料箱
// +X侧朝向传送带，方便工件从导料板滑入
// =====================================================
const storageBox = new THREE.Group();
storageBox.position.set(BELT_LEFT - 2.05, 0, BELT_Z);
scene.add(storageBox);

const binOuterMat = new THREE.MeshStandardMaterial({
 color:0x344b55, metalness:.84, roughness:.32
});
const binInnerMat = new THREE.MeshStandardMaterial({
 color:0x111e24, metalness:.55, roughness:.48
});
const binRimMat = new THREE.MeshStandardMaterial({
 color:0x9aa9ad, metalness:.94, roughness:.22
});
const binAccentMat = new THREE.MeshStandardMaterial({
 color:0x13a8b7, metalness:.72, roughness:.28,
 emissive:0x06343a
});

// 箱底与防滑内衬
box(storageBox,0,.28,0,3.25,.34,2.35,binOuterMat);
box(storageBox,0,.465,0,2.94,.035,2.04,binInnerMat);

// 后挡板及两侧挡板，朝向传送带的一端保持敞开
box(storageBox,-1.53,.91,0,.19,1.12,2.35,binOuterMat);
box(storageBox,0,.88,-1.08,3.12,1.02,.19,binOuterMat);
box(storageBox,0,.88,1.08,3.12,1.02,.19,binOuterMat);

// 箱口金属包边
box(storageBox,-1.53,1.49,0,.25,.085,2.34,binRimMat);
box(storageBox,0,1.49,-1.08,3.18,.085,.25,binRimMat);
box(storageBox,0,1.49,1.08,3.18,.085,.25,binRimMat);

// 外侧加强筋
for(const x of [-1.05,-.35,.35,1.05]){
 box(storageBox,x,.82,-1.19,.10,.72,.075,binRimMat);
 box(storageBox,x,.82,1.19,.10,.72,.075,binRimMat);
}

// 底部支撑脚
for(const x of [-1.20,1.20]){
 for(const z of [-.82,.82]){
  box(storageBox,x,.09,z,.32,.18,.32,binOuterMat);
 }
}

// 正面铭牌及状态色条
box(storageBox,-.20,.78,1.185,1.08,.28,.035,binInnerMat);
box(storageBox,-.20,.91,1.207,.78,.035,.018,binAccentMat);

// 传送带与收纳盒之间的金属导料滑槽
const feedChute = new THREE.Mesh(
 new THREE.BoxGeometry(1.35,.12,1.48),
 new THREE.MeshStandardMaterial({
  color:0x71858b, metalness:.90, roughness:.26
 })
);
feedChute.position.set(BELT_LEFT-.55,.60,BELT_Z);
feedChute.rotation.z=-.08;
feedChute.castShadow=true;
feedChute.receiveShadow=true;
scene.add(feedChute);


// 透明树脂/亚克力精密异形工件：参考用户图片的中央圆形凸台、双侧圆柱、
// 三角形安装翼、立式加强片与圆孔结构
const workpieces=[];
const acrylic=new THREE.MeshPhysicalMaterial({
 color:0xdce8e7,metalness:.18,roughness:.19,transmission:.42,
 transparent:true,opacity:.78,thickness:.32,ior:1.46,
 clearcoat:1,clearcoatRoughness:.12
});
const acrylicEdge=new THREE.MeshStandardMaterial({
 color:0xe9f1ef,metalness:.38,roughness:.22,transparent:true,opacity:.86
});
const innerMetal=mat(0x8b9da0,.78,.2),darkHole=mat(0x101a20,.25,.5);
function makeReferencePart(){
 const part=new THREE.Group();

 // 精密加工铝合金方形零件：银色金属表面、中心圆形沉孔、
 // 六角定位孔、四角安装凸台及环形加工槽
 const bodyMat=new THREE.MeshStandardMaterial({
  color:0x9ca5a8, metalness:.94, roughness:.24
 });
 const topMat=new THREE.MeshStandardMaterial({
  color:0xc5cbcd, metalness:.96, roughness:.19
 });
 const edgeMat=new THREE.MeshStandardMaterial({
  color:0x687277, metalness:.92, roughness:.29
 });
 const grooveMat=new THREE.MeshStandardMaterial({
  color:0x252d31, metalness:.82, roughness:.32
 });
 const brightMat=new THREE.MeshStandardMaterial({
  color:0xe1e5e6, metalness:.98, roughness:.16
 });

 function add(geo,material,x,y,z,rx=0,ry=0,rz=0){
  const mesh=new THREE.Mesh(geo,material);
  mesh.position.set(x,y,z);
  mesh.rotation.set(rx,ry,rz);
  mesh.castShadow=true;
  mesh.receiveShadow=true;
  part.add(mesh);
  return mesh;
 }

 // 方形主体底板，圆角倒边
 const shape=new THREE.Shape();
 const w=1.02, r=.16;
 shape.moveTo(-w+r,-w);
 shape.lineTo(w-r,-w);
 shape.quadraticCurveTo(w,-w,w,-w+r);
 shape.lineTo(w,w-r);
 shape.quadraticCurveTo(w,w,w-r,w);
 shape.lineTo(-w+r,w);
 shape.quadraticCurveTo(-w,w,-w,w-r);
 shape.lineTo(-w,-w+r);
 shape.quadraticCurveTo(-w,-w,-w+r,-w);
 const plateGeo=new THREE.ExtrudeGeometry(shape,{
  depth:.18, bevelEnabled:true, bevelSegments:3,
  steps:1, bevelSize:.045, bevelThickness:.035, curveSegments:12
 });
 add(plateGeo,bodyMat,0,-.09,0,-Math.PI/2,0,0);

 // 上表面薄金属盖板
 add(new THREE.BoxGeometry(1.88,.035,1.88),topMat,0,.115,0);

 // 四角阶梯形安装台和螺栓孔
 for(const x of [-.73,.73]){
  for(const z of [-.73,.73]){
   add(new THREE.BoxGeometry(.42,.09,.42),edgeMat,x,.16,z);
   add(new THREE.CylinderGeometry(.145,.16,.045,32),brightMat,x,.225,z);
   add(new THREE.CylinderGeometry(.092,.092,.012,32),grooveMat,x,.252,z);
   add(new THREE.CylinderGeometry(.052,.052,.014,6),edgeMat,x,.261,z);
  }
 }

 // 中央圆形加工台阶与深色沉孔
 add(new THREE.CylinderGeometry(.66,.70,.12,64),edgeMat,0,.19,0);
 add(new THREE.CylinderGeometry(.59,.62,.075,64),topMat,0,.275,0);

 add(new THREE.CylinderGeometry(.445,.46,.035,64),grooveMat,0,.315,0);
 add(new THREE.CylinderGeometry(.385,.40,.045,64),bodyMat,0,.342,0);


 // 中心六角凹槽及内孔
 add(new THREE.CylinderGeometry(.255,.255,.025,6),edgeMat,0,.375,0);
 add(new THREE.CylinderGeometry(.205,.205,.018,6),grooveMat,0,.391,0);
 add(new THREE.CylinderGeometry(.105,.105,.02,32),edgeMat,0,.402,0);
 add(new THREE.CylinderGeometry(.062,.062,.012,32),grooveMat,0,.414,0);

 // 四个方向的弧形加工槽，形成参考图的环绕式纹路
 for(let a=0;a<4;a++){
  const angle=a*Math.PI/2;
  const points=[];
  for(let j=0;j<=18;j++){
   const t=(-.72+j/18*1.44);
   const rr=.77;
   points.push(new THREE.Vector3(
    Math.cos(angle)*rr + Math.cos(angle+Math.PI/2)*t*.42,
    .151,
    Math.sin(angle)*rr + Math.sin(angle+Math.PI/2)*t*.42
   ));
  }
  const curve=new THREE.CatmullRomCurve3(points);
  add(new THREE.TubeGeometry(curve,32,.025,8,false),edgeMat,0,0,0);
  const highlightPoints=points.map(p=>new THREE.Vector3(p.x,.178,p.z));
  const highlightCurve=new THREE.CatmullRomCurve3(highlightPoints);
  add(new THREE.TubeGeometry(highlightCurve,32,.012,8,false),brightMat,0,0,0);
 }

 // 四周短槽及端部定位凸台
 for(let a=0;a<4;a++){
  const angle=a*Math.PI/2;
  const x=Math.cos(angle)*.82;
  const z=Math.sin(angle)*.82;
  const slot=add(new THREE.BoxGeometry(.48,.018,.13),grooveMat,x,.145,z,0,-angle,0);
  add(new THREE.BoxGeometry(.32,.012,.045),brightMat,x,.158,z,0,-angle,0);
 }

 // 边缘小型定位孔
 for(const x of [-.48,.48]){
  for(const z of [-.48,.48]){
   add(new THREE.CylinderGeometry(.055,.055,.018,24),edgeMat,x,.16,z);
   add(new THREE.CylinderGeometry(.027,.027,.02,24),grooveMat,x,.172,z);
  }
 }

 return part;
}
// 8件缩小后的工件，沿传送带上料端均匀排列
for(let i=0;i<8;i++){
 const group=makeReferencePart();
 // 工件中心间距扩大到3.0，减少金属件边缘接触和穿模
 group.position.set(10.0-i*3.0,1.00,BELT_Z);
 group.scale.set(.58,.58,.58);
 scene.add(group);
 group.userData={index:i,offset:i*3.0,state:'moving',bad:i===5||i===6,missing:i===5,classified:false};
 workpieces.push(group);
}
// 工业相机改为传送带侧装：位于传送带前侧，镜头水平朝向检测区域
// 这样不会挡住工件和机械臂，也能清楚看到相机与检测区域的对应关系
const cameraRig=new THREE.Group();cameraRig.position.set(-1.2,2.65,5.75);scene.add(cameraRig);
box(cameraRig,0,0,0,.82,.48,.62,dark);
const camLens=new THREE.Mesh(new THREE.CylinderGeometry(.17,.17,.34,24),mat(0x07131b,.7,.18));
camLens.rotation.x=Math.PI/2;camLens.position.set(0,0,.43);cameraRig.add(camLens);
const lensGlass=new THREE.Mesh(new THREE.CircleGeometry(.12,24),mat(0x12d8e8,.3,.15,0x087c9a));
lensGlass.position.set(0,0,.61);cameraRig.add(lensGlass);
// 侧装立柱与横向支架
box(scene,-1.2,1.25,5.75,.16,2.5,.16,steel);
box(scene,-1.2,2.25,6.15,.16,.14,.92,steel);
box(scene,-1.2,1.95,5.75,.72,.14,.72,dark);
const detectFrame=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(3.2,.05,1.55)),new THREE.LineBasicMaterial({color:0x14e8ee}));
detectFrame.position.set(-1.2,1.20,BELT_Z);scene.add(detectFrame);
const detectBeam=new THREE.SpotLight(0x00d9e8,5,5,Math.PI/5,.45,1.2);detectBeam.position.set(-1.2,2.55,6.32);detectBeam.target.position.set(-1.2,1.05,BELT_Z);scene.add(detectBeam);scene.add(detectBeam.target);
// 旁侧废品收集区，放在机械臂后侧并留出抓取空间
const rejectBin=new THREE.Group();rejectBin.position.set(-1.1,0,11.75);scene.add(rejectBin);
box(rejectBin,0,.48,0,2.2,.95,1.75,mat(0x57232a,.35,.5));
box(rejectBin,0,1.02,0,2.05,.12,1.62,mat(0xb72e36,.25,.35));
box(rejectBin,0,1.42,-.90,1.35,.72,.10,mat(0x241c25,.3,.5));
box(rejectBin,0,1.43,-.835,1.12,.46,.025,mat(0xff4545,.2,.3,0x7a1010),false);
// 三关节机械臂和夹爪
function makeRobot(x,z){
 const root=new THREE.Group();root.position.set(x,0,z);scene.add(root);
 // 参考协作机器人外观：银白色圆柱连杆、黑色关节外壳、紧凑平行夹爪
 const armMat=mat(0xdce4e6,.78,.23), jointMat=mat(0x202a30,.82,.25),
       trimMat=mat(0x8d9ba0,.8,.2),rubberMat=mat(0x11191e,.25,.65);
 function cyl(parent,rt,rb,h,material,y){
   const m=new THREE.Mesh(new THREE.CylinderGeometry(rt,rb,h,28),material);
   m.position.y=y;m.castShadow=true;m.receiveShadow=true;parent.add(m);return m;
 }
 function joint(parent,r,y){
   const g=new THREE.Group();g.position.y=y;parent.add(g);
   const ball=new THREE.Mesh(new THREE.SphereGeometry(r,28,20),jointMat);
   ball.castShadow=true;ball.receiveShadow=true;g.add(ball);
   const cap=new THREE.Mesh(new THREE.CylinderGeometry(r*.82,r*.82,r*.34,28),trimMat);
   cap.rotation.z=Math.PI/2;cap.castShadow=true;g.add(cap);
   return g;
 }
 // 固定立柱与底座
 const base=new THREE.Mesh(new THREE.CylinderGeometry(.66,.78,.34,32),dark);
 base.position.y=.18;base.castShadow=true;root.add(base);
 cyl(root,.29,.34,1.02,armMat,.82);
 cyl(root,.33,.33,.13,jointMat,1.34);
 const shoulder=new THREE.Group();shoulder.position.set(0,1.38,0);root.add(shoulder);
 // 肩部旋转关节 + 上臂圆柱
 joint(shoulder,.39,.02);
 cyl(shoulder,.235,.27,1.28,armMat,.70);
 cyl(shoulder,.275,.275,.12,trimMat,.70);
 const elbow=new THREE.Group();elbow.position.set(0,1.38,0);shoulder.add(elbow);
 // 肘关节采用横向圆盘外壳，形成参考图中的明显弯折结构
 joint(elbow,.34,.02);
 cyl(elbow,.205,.23,1.02,armMat,.52);
 cyl(elbow,.245,.245,.10,trimMat,.52);
 const wrist=new THREE.Group();wrist.position.set(0,1.02,0);elbow.add(wrist);
 // 腕部旋转壳体与末端法兰
 const wristJoint=new THREE.Mesh(new THREE.SphereGeometry(.25,24,18),jointMat);
 wristJoint.castShadow=true;wrist.add(wristJoint);
 const wristRing=new THREE.Mesh(new THREE.CylinderGeometry(.23,.23,.16,28),trimMat);
 wristRing.rotation.z=Math.PI/2;wrist.add(wristRing);
 box(wrist,0,-.19,.12,.34,.22,.34,armMat);
 // 银色平行夹爪：两指相向开合，指尖使用深色防滑块
 const fingerL=box(wrist,-.17,-.43,.20,.075,.34,.12,armMat);
 const fingerR=box(wrist,.17,-.43,.20,.075,.34,.12,armMat);
 box(wrist,-.17,-.59,.20,.095,.08,.15,rubberMat);
 box(wrist,.17,-.59,.20,.095,.08,.15,rubberMat);
 // 关节装饰环，让各段更接近工业协作机械臂的金属外观
 cyl(shoulder,.255,.255,.07,jointMat,.23);
 cyl(elbow,.225,.225,.07,jointMat,.20);
 return {root,shoulder,elbow,wrist,fingerL,fingerR};
}
const robot=makeRobot(-1.1,9.75);
let totalDetected=0,goodDetected=0,badDetected=0,missingDetected=0,rejectStored=0,activePick=null;
function updateProductionBoard(){
 const el=id=>document.getElementById(id);
 el('output').textContent=(1286+totalDetected).toLocaleString('en-US');el('bottomOutput').textContent=(1286+totalDetected).toLocaleString('en-US');
 el('goodCount').textContent=1264+goodDetected;el('badCount').textContent=22+badDetected;el('missingCount').textContent=8+missingDetected;
 el('rejectBinCount').textContent=rejectStored;el('yieldRate').textContent=((1264+goodDetected)/(1286+totalDetected)*100).toFixed(1);
}
function logSort(message){const el=document.getElementById('sortLog');if(el)el.innerHTML=message+'<br>'+el.innerHTML.split('<br>').slice(0,2).join('<br>');}

// 工件补料安全检查：入口有足够空位才重新出现，避免重生时与其他工件重叠
function tryRespawnPart(part){
 const spawnX=10.0;
 for(const other of workpieces){
  if(other===part || !other.visible)continue;
  if(other.userData.state==='stored' || other.userData.state==='waitingSpawn')continue;
  if(Math.abs(other.position.x-spawnX)<3.0 &&
     Math.abs(other.position.z-BELT_Z)<.45){
   return false;
  }
 }
 part.position.set(spawnX,1.02,BELT_Z);
 part.visible=true;
 part.userData.classified=false;
 part.userData.state='moving';
 part.userData.bad=Math.random()<.30;
 part.userData.missing=part.userData.bad&&Math.random()<.5;
 part.userData.pickT=0;
 part.userData.storedT=0;
 return true;
}

function classifyPart(part){
 if(part.userData.classified)return;
 part.userData.classified=true;totalDetected++;document.getElementById('detectCount').textContent=totalDetected;
 document.getElementById('detectState').textContent=part.userData.bad?'发现缺陷':'合格';
 if(part.userData.bad){
  badDetected++;if(part.userData.missing)missingDetected++;
  // 工件停在机械臂正前方的固定抓取点，避免机械臂追逐移动工件
  part.position.set(-1.1,1.12,BELT_Z);
  part.userData.state='rejecting';part.userData.pickT=0;
  part.userData.pickStart=new THREE.Vector3(-1.1,1.12,BELT_Z);
  activePick=part;
  logSort('<span style="color:#ff6b70">缺陷报警：工件 #'+(part.userData.index+1)+'，机械臂准备抓取</span>');
 }
 else{goodDetected++;part.userData.state='passed';logSort('<span style="color:#42e6bd">工件 #'+(part.userData.index+1)+' 检测合格，继续输送</span>');}
 updateProductionBoard();
}
// 厂房支撑架整体向后移动，六台机床本身的位置、尺寸和朝向不变
// 相比原位置，前后两排支撑架均向-Z方向移动2.5
const FRAME_BACK_Z=-17.0;
const FRAME_FRONT_Z=10.5;
const FRAME_CENTER_Z=(FRAME_BACK_Z+FRAME_FRONT_Z)/2;
const FRAME_DEPTH=FRAME_FRONT_Z-FRAME_BACK_Z;

for(let x=-13;x<=13;x+=6.5){
 for(let z of [FRAME_BACK_Z,FRAME_FRONT_Z]){
  box(scene,x,5,z,.25,10,.25,steel);
 }
 // 顶部纵向连接梁随立柱跨度同步调整
 box(scene,x,9.9,FRAME_CENTER_Z,.22,.22,FRAME_DEPTH,steel);
}
// 前后顶部横梁
for(let z of [FRAME_BACK_Z,FRAME_FRONT_Z]){
 box(scene,0,9.8,z,27,.25,.25,steel);
}

// 设备状态灯
const lamps=[];
machines.forEach((m,i)=>{
 const l=new THREE.Mesh(new THREE.SphereGeometry(.12,12,12),new THREE.MeshBasicMaterial({color:i===2?0xffb52e:0x13f2c1}));
 l.position.set(m.position.x,m.position.y+3.3,m.position.z);scene.add(l);lamps.push(l);
});

function animate(){
 requestAnimationFrame(animate);
 const t=performance.now()*.001;
 if(activePick){
  const p=activePick;p.userData.pickT+=.012;const q=Math.min(p.userData.pickT,1);
  const p0=p.userData.pickStart;
  const grip=new THREE.Vector3(-1.1,1.34,BELT_Z);       // 夹爪抬离传送带
  const lifted=new THREE.Vector3(-1.1,2.0,7.95);
  const carry=new THREE.Vector3(-1.1,1.95,10.75);     // 抬高后绕过传送带侧边
  const drop=new THREE.Vector3(-1.1,1.32,11.65);      // 废品箱投放口
  if(q<.22){
   const k=q/.22;robot.shoulder.rotation.x=-1.05*k;robot.elbow.rotation.x=.62*k;
   robot.fingerL.position.x=-.19+.10*k;robot.fingerR.position.x=.19-.10*k;
   p.position.lerpVectors(p0,grip,k);
  }else if(q<.42){
   const k=(q-.22)/.20;robot.shoulder.rotation.x=-1.05-.10*k;robot.elbow.rotation.x=.62-.12*k;
   p.position.lerpVectors(grip,lifted,k);
  }else if(q<.72){
   const k=(q-.42)/.30;robot.shoulder.rotation.x=-1.15+2.05*k;robot.elbow.rotation.x=.50-.85*k;
   p.position.lerpVectors(lifted,carry,k);
  }else if(q<.90){
   const k=(q-.72)/.18;robot.shoulder.rotation.x=.90-.08*k;robot.elbow.rotation.x=-.35+.07*k;
   p.position.lerpVectors(carry,drop,k);
  }else{
   const k=(q-.90)/.10;robot.shoulder.rotation.x=.82*(1-k);robot.elbow.rotation.x=-.28*(1-k);
   p.position.lerpVectors(drop,new THREE.Vector3(-1.1,1.05,11.75),k);
   robot.fingerL.position.x=-.09-.10*k;robot.fingerR.position.x=.09+.10*k;
  }
  robot.wrist.rotation.x=-.10;
  if(q>=1){p.visible=false;p.userData.state='stored';p.userData.storedT=0;rejectStored++;activePick=null;robot.shoulder.rotation.x=0;robot.elbow.rotation.x=0;robot.wrist.rotation.x=0;robot.fingerL.position.x=-.19;robot.fingerR.position.x=.19;logSort('<span style="color:#ff7777">缺陷件已投入旁侧废品箱</span>');updateProductionBoard();}
 }else{robot.shoulder.rotation.x=Math.sin(t*1.2)*.035;robot.elbow.rotation.x=.10+Math.sin(t*1.2+1)*.025;robot.wrist.rotation.x=Math.sin(t*.9)*.025;}
 beltRollers.forEach(roller=>{roller.rotation.x-=.045;});
 workpieces.forEach(part=>{
  // 分拣完成的工件短暂进入废品箱后，模拟新工件补料，重新回到传送带入口
  if(part.userData.state==='stored'){
   part.userData.storedT=(part.userData.storedT||0)+.016;
   if(part.userData.storedT>1.35){
    part.userData.state='waitingSpawn';
    part.visible=false;
    tryRespawnPart(part);
   }
   return;
  }
  if(part.userData.state==='waitingSpawn'){
   tryRespawnPart(part);
   return;
  }
  if(part.userData.state==='rejecting')return;
  if(part.userData.state==='queued'){
   if(!activePick){part.userData.state='moving';classifyPart(part);}
   return;
  }
  if(part.userData.state==='moving'||part.userData.state==='passed'){
   // 防追尾：运动方向为-X，前方工件不足3.0间距时暂停当前工件
   let blockedByPart=false;
   for(const other of workpieces){
    if(other===part || !other.visible)continue;
    if(other.userData.state==='stored' || other.userData.state==='waitingSpawn')continue;
    const gap=part.position.x-other.position.x;
    if(gap>0 && gap<3.0 &&
       Math.abs(part.position.z-other.position.z)<.45){
     blockedByPart=true;
     break;
    }
   }
   if(!blockedByPart)part.position.x-=.012;

   if(!part.userData.classified&&part.position.x<=-1.1){
    if(activePick&&part.userData.bad){part.position.x=-1.1;part.userData.state='queued';}
    else classifyPart(part);
   }
   // 到达传送带左端后等待入口空位，再安全循环补料
   if(part.position.x<BELT_LEFT+.25){
    part.userData.state='waitingSpawn';
    part.visible=false;
    tryRespawnPart(part);
   }
  }
 });
 detectFrame.material.opacity=.55+.45*Math.sin(t*3);detectFrame.material.transparent=true;detectBeam.intensity=4+1.5*Math.sin(t*4);
 controls.update();renderer.render(scene,camera);
}
animate();
addEventListener('resize',()=>{
 camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();
 renderer.setSize(innerWidth,innerHeight);
});
</script>

<script>
let auto=true;
function updateClock(){
 const d=new Date();
 document.getElementById('clock').textContent=d.toLocaleDateString('zh-CN')+' '+d.toLocaleTimeString('zh-CN',{hour12:false});
}
updateClock();setInterval(updateClock,1000);
function toggleAuto(){
 auto=!auto;
 const b=document.getElementById('autoBtn');
 b.classList.toggle('active',auto);
 b.textContent=auto?'自动监测':'暂停监测';
 showToast(auto?'已开启自动监测':'已暂停自动监测');
}
function selectDevice(el,name){
 document.querySelectorAll('.device').forEach(x=>x.classList.remove('selected'));
 el.classList.add('selected');
 document.getElementById('modalTitle').textContent=name;
 document.getElementById('modalBody').innerHTML='<p>设备状态：运行中</p><p>所属产线：智能加工生产线 01</p><p>当前工序：工件输送 / 自动加工</p><p>提示：当前参数为界面演示数据，接入真实设备后可显示现场数据。</p><button class="action" onclick="showToast(\'已发送设备状态刷新请求\')">刷新设备数据</button><button class="action" onclick="toggleDeviceState(this)">切换启停状态</button>';
 openPanel('device');
}
function toggleDeviceState(btn){
 const running=btn.textContent.includes('切换启停');
 btn.textContent=running?'设备已暂停（点击恢复）':'切换启停状态';
 showToast(running?'演示设备已暂停':'演示设备已恢复运行');
}
function openPanel(type){
 const mask=document.getElementById('modalMask'),title=document.getElementById('modalTitle'),body=document.getElementById('modalBody');
 if(type==='monitor'){
  title.textContent='生产线数据监测';
  body.innerHTML='<p>主轴转速：'+document.getElementById('rpm').textContent+' rpm</p><p>主轴负载：'+document.getElementById('load').textContent+'%</p><p>设备温度：'+document.getElementById('temp').textContent+' ℃</p><p>视觉相机：CAM-01 在线</p><p>检测结果为演示数据；接入 ONNX 模型后显示真实识别类别与置信度。</p>';
 }else if(type==='inspect'){
  title.textContent='设备巡检任务';
  body.innerHTML='<p>巡检对象：A01 数控加工中心、CAM-01 工业相机、传送带 D04、机械臂 C03</p><p>巡检项目：设备在线状态、温度、运行负载、相机画面、输送线运行情况。</p><p id="inspectResult">待执行巡检。</p><button class="action" onclick="runInspection()">开始巡检</button>';
 }else if(type==='device'){
  // 设备详情内容已由 selectDevice 填充
 }
 mask.classList.add('show');
}
function runInspection(){
 document.getElementById('inspectResult').textContent='巡检完成：演示环境下设备状态正常，相机在线，输送线运行中。';
 showToast('设备巡检已完成');
}
function closePanel(e){if(!e||e.target.id==='modalMask')document.getElementById('modalMask').classList.remove('show');}
function resetCameraView(){window.dispatchEvent(new Event('reset-twin-camera'));showToast('3D视角已复位');}
function showToast(msg){
 const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');
 clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>t.classList.remove('show'),1800);
}
setInterval(()=>{
 if(!auto)return;
 document.getElementById('rpm').textContent=3200+Math.floor(Math.random()*45-22);
 document.getElementById('load').textContent=66+Math.floor(Math.random()*6);
 document.getElementById('temp').textContent=(36.3+Math.random()*.6).toFixed(1);
},1800);
</script>
</body>
</html>
"""

components.html(html, height=980, scrolling=False)
