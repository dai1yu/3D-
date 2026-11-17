import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="智能工厂数字孪生平台｜零件改版+多机床增强版",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, footer, header, [data-testid="stToolbar"] {visibility: hidden;}
    .stApp {background: #06121b;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0;}
</style>
""", unsafe_allow_html=True)


def render_twin_html():
    html = r'''
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
#loadingMask{position:absolute;inset:0;z-index:99;background:#06121b;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:16px;color:#16d9df}
#loadingMask.hide{display:none;}
.load-spinner{width:48px;height:48px;border:3px solid rgba(22,217,223,0.2);border-top-color:#16d9df;border-radius:50%;animation:spin 1s linear infinite;}
@keyframes spin{to{transform:rotate(360deg);}}
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
.panel{position:absolute;z-index:3;width:280px;background:linear-gradient(135deg,rgba(3,26,37,.92),rgba(3,18,29,.77));
border:1px solid var(--line);box-shadow:0 0 20px rgba(0,207,222,.10),inset 0 0 22px rgba(0,150,170,.08);
padding:14px 14px 12px;backdrop-filter:blur(8px)}
.panel:before,.panel:after{content:"";position:absolute;width:35px;height:2px;background:var(--cyan);box-shadow:0 0 8px var(--cyan)}
.panel:before{left:-1px;top:-1px}.panel:after{right:-1px;bottom:-1px}
.left{left:18px;top:88px;bottom:128px;overflow-y:auto}
.right{right:18px;top:88px;bottom:128px}
.panel-title{font-size:14px;letter-spacing:2px;color:#b8faff;border-bottom:1px solid rgba(38,211,221,.32);
padding:0 0 11px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center}
.panel-title span{font-size:10px;color:#5bcbd3;letter-spacing:1px}
.section-label{font-size:11px;color:#57c8d1;margin:13px 0 8px;display:flex;align-items:center;gap:8px}
.section-label:before{content:"";width:5px;height:5px;background:#19dce2;box-shadow:0 0 8px #19dce2}
.device{display:flex;justify-content:space-between;align-items:center;padding:9px 8px;margin:4px 0;
border:1px solid rgba(27,170,185,.18);background:rgba(12,73,86,.18);font-size:11px;color:#b8dfe3;cursor:pointer}
.device:hover,.device.selected{border-color:#14dce3;background:rgba(0,175,190,.22);color:#e1ffff}
.dot{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:7px;background:#23e7a5;box-shadow:0 0 8px #23e7a5}
.dot.warn{background:#ffba45;box-shadow:0 0 8px #ffba45}
.dot.off{background:#768a91;box-shadow:none}
.status{color:#39e9bd;font-size:10px}
.status.warn{color:#ffc15b}
.status.off{color:#88989e}
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
.modal-mask{display:none;position:absolute;z-index:10;inset:0;background:rgba(0,8,15,.68);align-items:center;justify-content:center}
.modal-mask.show{display:flex}.modal{width:min(520px,90vw);border:1px solid #16d9df;background:linear-gradient(145deg,#082b38,#061722);box-shadow:0 0 35px #087b8a;padding:18px}
.modal-head{display:flex;justify-content:space-between;align-items:center;color:#cfffff;border-bottom:1px solid rgba(22,217,223,.35);padding-bottom:12px}
.close-btn{background:transparent;color:#8ffaff;border:1px solid #168ba8;padding:5px 10px;cursor:pointer}
.modal-body{font-size:13px;line-height:2;color:#a9dce1;padding-top:12px}.modal-body button{margin:6px 8px 0 0}
.modal-body .action{border:1px solid #16d9df;background:rgba(0,160,175,.18);color:#cfffff;padding:8px 12px;cursor:pointer}
.tooltip{position:absolute;z-index:11;left:50%;top:50%;transform:translate(-50%,-50%);padding:16px 24px;
background:rgba(3,35,44,.94);border:1px solid #16d9df;box-shadow:0 0 20px #087b8a;display:none;font-size:13px}
.tooltip.show{display:block}
@media(max-width:1300px){
 .panel{width:240px}.left{left:8px}.right{right:8px}
 .bottom{left:8px;right:8px;gap:5px}.bottom-card{padding:9px 7px}
 .bottom-card strong{font-size:17px}.brand{font-size:17px}
 .top-actions{gap:4px;}
 .top-btn{padding:6px 8px;font-size:11px;}
}
</style>
</head>
<body>
<div id="app">
<div id="loadingMask">
 <div class="load-spinner"></div>
 <div>3D工厂场景加载中...</div>
 <div id="loadErr" style="color:#ff7470;font-size:12px;display:none">Three.js加载失败，请检查网络连接</div>
</div>
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
  <div class="device selected" onclick="selectDevice(this,'数控加工中心 A01')"><span><i class="dot" id="dotA01"></i>数控加工中心 A01</span><b class="status" id="statA01">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A02')"><span><i class="dot" id="dotA02"></i>数控加工中心 A02</span><b class="status" id="statA02">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A03')"><span><i class="dot warn" id="dotA03"></i>数控加工中心 A03</span><b class="status warn" id="statA03">待机</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A04')"><span><i class="dot" id="dotA04"></i>数控加工中心 A04</span><b class="status" id="statA04">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A05')"><span><i class="dot" id="dotA05"></i>数控加工中心 A05</span><b class="status" id="statA05">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A06')"><span><i class="dot warn" id="dotA06"></i>数控加工中心 A06</span><b class="status warn" id="statA06">待机</b></div>
  <div class="device" onclick="selectDevice(this,'数控加工中心 A07')"><span><i class="dot" id="dotA07"></i>数控加工中心 A07</span><b class="status" id="statA07">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控车床 B02')"><span><i class="dot" id="dotB02"></i>数控车床 B02</span><b class="status" id="statB02">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控车床 B03')"><span><i class="dot" id="dotB03"></i>数控车床 B03</span><b class="status" id="statB03">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'数控车床 B04')"><span><i class="dot warn" id="dotB04"></i>数控车床 B04</span><b class="status warn" id="statB04">待机</b></div>
  <div class="device" onclick="selectDevice(this,'数控车床 B05')"><span><i class="dot" id="dotB05"></i>数控车床 B05</span><b class="status" id="statB05">运行中</b></div>
  <div class="device" onclick="selectDevice(this,'检测工作站 E05')"><span><i class="dot off" id="dotE05"></i>检测工作站 E05</span><b class="status off" id="statE05">离线</b></div>

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
  <div class="section-label">缺陷分拣统计</div>
  <div class="metric-grid">
    <div class="metric"><label>缺件数量</label><strong id="missingCount">8</strong><em>件</em></div>
    <div class="metric"><label>废品暂存区</label><strong id="rejectBinCount">0</strong><em>件</em></div>
  </div>
  <div class="section-label">能源消耗监测</div>
  <div class="bar-row"><span>电力</span><div class="bar"><i style="width:72%"></i></div><b>72%</b></div>
  <div class="bar-row"><span>压缩空气</span><div class="bar"><i style="width:48%"></i></div><b>48%</b></div>
  <div class="bar-row"><span>冷却液</span><div class="bar"><i style="width:35%"></i></div><b>35%</b></div>
  <div class="section-label">实时分拣记录</div>
  <div id="sortLog" style="font-size:10px;color:#8ecbd0;line-height:2.1;max-height:130px;overflow-y:auto">等待首件进入视觉检测区…</div>
</div>
<div class="bottom">
 <div class="bottom-card"><label>当前生产任务</label><strong>加工任务 #0826</strong><span class="spark">▰</span></div>
 <div class="bottom-card"><label>设备总数 / 在线设备</label><strong>24 / 22</strong><small>台</small></div>
 <div class="bottom-card"><label>今日生产数量</label><strong id="bottomOutput">1,286</strong><small>件</small></div>
 <div class="bottom-card"><label>平均加工效率</label><strong>96.8</strong><small>%</small></div>
 <div class="bottom-card"><label>系统运行状态</label><strong id="sysStatus" style="color:#39e8b6">正常</strong><small>ALL SYSTEMS GO</small></div>
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
<script>
const SIM_CONFIG = {
 speedRate: 1.0,
 defectRate: 0.30,
 autoStart: true,
 soundAlert: false
};
let sortLogRecords = [];
let audioCtx = null;
let SIM_RUNNING = SIM_CONFIG.autoStart;
function playBeepAlert(){
    if(!SIM_CONFIG.soundAlert) return;
    try{
        if(!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.type = "square";
        osc.frequency.value = 880;
        gain.gain.value = 0.12;
        osc.start();
        osc.stop(audioCtx.currentTime + 0.22);
    }catch(e){}
}
function id(name){return document.getElementById(name);}
function showLoadingDone(){id("loadingMask").classList.add("hide");}
function showLoadErr(){id("loadErr").style.display="block";}
let auto = SIM_CONFIG.autoStart;
function updateClock(){
 const d=new Date();
 id('clock').textContent=d.toLocaleDateString('zh-CN')+' '+d.toLocaleTimeString('zh-CN',{hour12:false});
}
updateClock();setInterval(updateClock,1000);
function toggleAuto(){
 auto=!auto;
 SIM_RUNNING = auto;
 const b=id('autoBtn');
 b.classList.toggle('active',auto);
 b.textContent=auto?'自动监测':'暂停监测';
 showToast(auto?'✅ 已开启自动监测，产线开始运行':'⏸️ 已暂停自动监测，产线停止');
}
let selectedDeviceName = "";
function selectDevice(el,name){
 selectedDeviceName = name;
 document.querySelectorAll('.device').forEach(x=>x.classList.remove('selected'));
 el.classList.add('selected');
 id('modalTitle').textContent=name;
 id('modalBody').innerHTML=`
 <p>设备名称：${name}</p>
 <p>所属产线：智能加工生产线 01</p>
 <p>当前状态：<span id="devStateText">运行中</span></p>
 <p>提示：点击下方按钮切换启停状态</p>
 <button class="action" onclick="refreshDeviceData()">刷新设备数据</button>
 <button class="action" onclick="toggleDeviceState()">切换启停状态</button>`;
 openPanel('device');
}
function toggleDeviceState(){
 const devName = selectedDeviceName;
 let dotId, statId;
 if(devName.indexOf("A01")>-1){dotId="dotA01";statId="statA01";}
 else if(devName.indexOf("A02")>-1){dotId="dotA02";statId="statA02";}
 else if(devName.indexOf("A03")>-1){dotId="dotA03";statId="statA03";}
 else if(devName.indexOf("A04")>-1){dotId="dotA04";statId="statA04";}
 else if(devName.indexOf("A05")>-1){dotId="dotA05";statId="statA05";}
 else if(devName.indexOf("A06")>-1){dotId="dotA06";statId="statA06";}
 else if(devName.indexOf("A07")>-1){dotId="dotA07";statId="statA07";}
 else if(devName.indexOf("B02")>-1){dotId="dotB02";statId="statB02";}
 else if(devName.indexOf("B03")>-1){dotId="dotB03";statId="statB03";}
 else if(devName.indexOf("B04")>-1){dotId="dotB04";statId="statB04";}
 else if(devName.indexOf("B05")>-1){dotId="dotB05";statId="statB05";}
 else if(devName.indexOf("E05")>-1){dotId="dotE05";statId="statE05";}
 else {showToast("未匹配设备");return;}
 const dot = id(dotId);
 const stat = id(statId);
 const stateText = id("devStateText");
 if(dot.classList.contains("off")){
    dot.className="dot";
    stat.className="status";
    stat.innerText="运行中";
    stateText.innerText="运行中";
    showToast(devName+" 已启动");
 }else{
    dot.className="dot off";
    stat.className="status off";
    stat.innerText="已停止";
    stateText.innerText="已停机";
    showToast(devName+" 已停机");
 }
}
function refreshDeviceData(){
 id('rpm').textContent=3200+Math.floor(Math.random()*45-22);
 id('load').textContent=66+Math.floor(Math.random()*6);
 id('temp').textContent=(36.3+Math.random()*.6).toFixed(1);
 showToast("🔄 设备数据已刷新");
}
function openPanel(type){
 const mask=id('modalMask'),title=id('modalTitle'),body=id('modalBody');
 if(type==='monitor'){
  title.textContent='生产线数据监测';
  body.innerHTML=`
  <p>主轴转速：${id('rpm').textContent} rpm</p>
  <p>主轴负载：${id('load').textContent}%</p>
  <p>设备温度：${id('temp').textContent} ℃</p>
  <p>视觉相机：CAM-01 在线</p>
  <p>检测结果为演示数据；接入 ONNX 模型后显示真实识别类别与置信度。</p>
  <button class="action" onclick="refreshDeviceData()">刷新实时参数</button>`;
 }else if(type==='inspect'){
  title.textContent='设备巡检任务';
  body.innerHTML=`
  <p>巡检对象：A01‑A07、B02‑B05、E05、CAM‑01、传送带 D04、机械臂 C03</p>
  <p>巡检项目：设备在线状态、温度、运行负载、相机画面、输送线运行情况。</p>
  <p id="inspectResult">待执行巡检。</p>
  <button class="action" onclick="runInspection()">开始巡检</button>`;
 }
 mask.classList.add('show');
}
function runInspection(){
 const resEl = id('inspectResult');
 resEl.textContent = "✅ 巡检完成：A01,A02,A04,A05,A07运行正常；A03,A06待机；B02,B03,B05运行正常；B04待机，E05离线；相机通信正常，无异常报警。";
 showToast("设备巡检已完成");
}
function closePanel(e){if(!e||e.target.id==='modalMask')id('modalMask').classList.remove('show');}
function resetCameraView(){window.dispatchEvent(new Event('reset-twin-camera'));showToast('3D视角已复位');}
function showToast(msg){
 const t=id('toast');t.textContent=msg;t.classList.add('show');
 clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>t.classList.remove('show'),1800);
}
setInterval(()=>{
 if(!auto)return;
 refreshDeviceData();
},1800);
window.addEventListener('load',()=>{
 setTimeout(()=>{
    if(!window.THREE) showLoadErr();
 },3500);
});
</script>
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';
window.THREE = THREE;
const canvas=document.querySelector('#scene');
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(innerWidth,innerHeight);
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.25;
const scene=new THREE.Scene();
scene.background=new THREE.Color(0x061722);
scene.fog=new THREE.Fog(0x061722,30,80);
const camera=new THREE.PerspectiveCamera(45,innerWidth/innerHeight,.1,200);
camera.position.set(26,20,30);
const controls=new OrbitControls(camera,renderer.domElement);
controls.target.set(0,1,0);
controls.enableDamping=true;
controls.enablePan=true;
controls.minDistance=14;controls.maxDistance=60;
controls.maxPolarAngle=Math.PI*.50;
const defaultCameraPosition=new THREE.Vector3(26,20,30);
window.addEventListener('reset-twin-camera',()=>{
 camera.position.copy(defaultCameraPosition);controls.target.set(0,1,0);controls.update();
});
scene.add(new THREE.HemisphereLight(0xa8efff,0x14252d,2.2));
const key=new THREE.DirectionalLight(0xffffff,2.5);
key.position.set(14,26,14);key.castShadow=true;scene.add(key);
const cyanLight=new THREE.PointLight(0x00d9e8,34,40);cyanLight.position.set(-12,9,2);scene.add(cyanLight);
const blueLight=new THREE.PointLight(0x087bff,24,36);blueLight.position.set(12,7,-10);scene.add(blueLight);

// PBR材质库
const mat=(color,metalness=.25,roughness=.55,emissive=0x000000)=>new THREE.MeshStandardMaterial({color,metalness,roughness,emissive});
const floorMat=mat(0x142d35,.22,.84);
const floor=new THREE.Mesh(new THREE.PlaneGeometry(64,48),floorMat);
floor.rotation.x=-Math.PI/2;floor.position.y=-.08;floor.receiveShadow=true;scene.add(floor);
const grid=new THREE.GridHelper(64,64,0x087e91,0x164451);grid.position.y=-.045;scene.add(grid);

function box(parent,x,y,z,w,h,d,material,cast=true){
 const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material);
 m.position.set(x,y,z);m.castShadow=cast;m.receiveShadow=true;parent.add(m);return m;
}
function cyl(parent,rt,rb,h,material,x,y,z){
 const geo=new THREE.CylinderGeometry(rt,rb,h,32);
 const mesh=new THREE.Mesh(geo,material);
 mesh.position.set(x,y,z);mesh.castShadow=true;mesh.receiveShadow=true;parent.add(mesh);return mesh;
}

const dark=mat(0x182d37,.72,.32);
const steel=mat(0x8c9ca4,.78,.24);
const steelLight=mat(0xb8c4c9,.65,.22);
const white=mat(0xc4d4d5,.35,.38);
const glass=new THREE.MeshStandardMaterial({color:0x0a7180,metalness:.25,roughness:.12,transparent:true,opacity:.50});
const yellow=mat(0xf0aa24,.45,.4);
const glow=mat(0x00cbd8,.3,.25,0x006b77);
const redAlert=mat(0xdd3333,.4,.3);
const blackPlastic=mat(0x0c0f14,.2,.45);
const panelGray=mat(0x48545a,.6,.30);

// ===================== 增强版CNC加工中心，增加操作面板、悬臂、散热格栅、排屑口 =====================
function makeMachine(x,z,label){
 const g=new THREE.Group();
 g.position.set(x,0,z);
 scene.add(g);
 //底座
 box(g, 0,0.40,0, 4.4,0.82,3.2, dark);
 //地脚
 for(let dx of [-2.0,2.0]) for(let dz of [-1.45,1.45]){
    box(g,dx,0.13,dz,0.48,0.24,0.48,blackPlastic);
 }
 //机身壳体
 box(g,0,1.42,0,4.0,1.65,2.8, steel);
 //主观察钢化玻璃门
 box(g,0,1.48,1.55,3.6,1.44,0.14,steelLight);
 box(g,0,1.52,1.62,3.4,1.36,0.07,glass,false);
 //铰链
 box(g,-1.78,1.60,1.64,0.12,0.6,0.08,panelGray);
 box(g,1.78,1.60,1.64,0.12,0.6,0.08,panelGray);
 //排屑槽开口
 box(g,0,0.75,-1.40,2.2,0.22,0.7,blackPlastic);
 //主轴箱上部
 box(g,0,2.50,0,1.5,1.40,1.2,dark);
 //主轴套筒
 cyl(g,0.24,0.24,0.80,steel,0,3.12,0);
 //三色警示灯立柱
 cyl(g,0.68,0.68,0.30,dark,-1.5,2.52,0);
 cyl(g,0.16,0.16,0.65,steel,-1.5,3.05,0);
 cyl(g,0.13,0.13,0.24,redAlert,-1.5,3.45,0);
 cyl(g,0.13,0.13,0.24,mat(0xffcc22,.5,.2),-1.5,3.74,0);
 cyl(g,0.13,0.13,0.24,mat(0x30dd60,.5,.2),-1.5,4.03,0);
 //操作悬臂+控制面板
 box(g,2.1,1.70,0.7,0.24,0.90,0.80, blackPlastic);
 box(g,2.14,1.74,0.76,0.16,0.66,0.52,glow,false);
 box(g,2.60,2.10,0.90,0.12,0.70,0.55,panelGray);
 //侧面散热格栅
 for(let sy=0; sy<5; sy++){
    box(g,-2.10,1.10+sy*0.28,0,0.06,0.14,2.4,blackPlastic);
 }
 g.userData.label=label;
 return g;
}

// =====================增强版数控车床 =====================
function makeLathe(x,z,label){
 const g=new THREE.Group();
 g.position.set(x,0,z);
 scene.add(g);
 box(g,0,0.44,0,3.8,0.86,2.6,dark);
 for(let dx of [-1.65,1.65]) for(let dz of [-1.15,1.15]){
    box(g,dx,0.14,dz,0.44,0.26,0.44,blackPlastic);
 }
 box(g,0,1.38,0,3.4,1.50,2.3,steel);
 box(g,0,1.44,1.32,3.0,1.30,0.11,steelLight);
 box(g,0,1.48,1.38,2.8,1.22,0.06,glass,false);
 box(g,-1.2,2.20,0,1.05,1.10,0.90,dark);
 cyl(g,0.30,0.30,0.60,steel,-1.2,2.74,0);
 box(g,1.7,1.60,0.45,0.22,0.82,0.70,blackPlastic);
 box(g,1.73,1.64,0.50,0.14,0.60,0.46,glow,false);
 cyl(g,0.14,0.14,0.55,steel,0,3.70,0);
 cyl(g,0.12,0.12,0.22,redAlert,0,4.10,0);
 cyl(g,0.12,0.12,0.22,mat(0xffcc22,.5,.2),0,4.38,0);
 cyl(g,0.12,0.12,0.22,mat(0x30dd60,.5,.2),0,4.66,0);
 //散热格栅
 for(let sy=0; sy<4; sy++){
    box(g,1.90,1.15+sy*0.30,-0.60,0.06,0.16,1.8,blackPlastic);
 }
 g.userData.label=label;
 return g;
}

//增强检测工作站
function makeStation(x,z,label){
 const g=new THREE.Group();
 g.position.set(x,0,z);
 scene.add(g);
 box(g,0,0.42,0,3.6,0.84,2.8,dark);
 for(let dx of [-1.55,1.55]) for(let dz of [-1.20,1.20]){
    box(g,dx,0.13,dz,0.44,0.24,0.44,blackPlastic);
 }
 box(g,0,1.34,0,3.2,1.36,2.4,steel);
 box(g,0,1.42,1.34,2.8,1.22,0.11,steelLight);
 box(g,0,1.46,1.40,2.6,1.14,0.06,glass,false);
 box(g,0,2.40,0,1.3,1.05,0.95,dark);
 cyl(g,0.20,0.20,0.44,steel,0,2.96,0);
 box(g,1.7,1.54,0.44,0.24,0.86,0.72,blackPlastic);
 box(g,1.74,1.58,0.50,0.14,0.64,0.48,glow,false);
 cyl(g,0.14,0.14,0.60,steel,0,3.88,0);
 cyl(g,0.12,0.12,0.24,redAlert,0,4.30,0);
 cyl(g,0.12,0.12,0.24,mat(0xffcc22,.5,.2),0,4.60,0);
 cyl(g,0.12,0.12,0.24,mat(0x30dd60,.5,.2),0,4.90,0);
 g.userData.label=label;
 return g;
}

// ============扩充机床数量：7台CNC，4台车床，1台检测站，重新布局============
const machines=[
 makeMachine(12,8,'数控加工中心 A01'),
 makeMachine(12,0,'数控加工中心 A02'),
 makeMachine(12,-8,'数控加工中心 A03'),
 makeMachine(2,10,'数控加工中心 A04'),
 makeMachine(2,2,'数控加工中心 A05'),
 makeMachine(2,-6,'数控加工中心 A06'),
 makeMachine(-8,8,'数控加工中心 A07'),

 makeLathe(-8,0,'数控车床 B02'),
 makeLathe(-8,-8,'数控车床 B03'),
 makeLathe(-18,6,'数控车床 B04'),
 makeLathe(-18,-4,'数控车床 B05'),

 makeStation(-18,-12,'检测工作站 E05')
];

//传送带
const beltMat=mat(0x253f49,.65,.4);
box(scene,-1.1,.43,5.35,14.0,.54,1.75,beltMat);
box(scene,-1.1,.74,5.35,13.6,.09,1.42,mat(0x0a5963,.5,.3));
const beltRollers=[];
for(let i=0;i<15;i++){
 const roller=new THREE.Mesh(new THREE.CylinderGeometry(.13,.13,1.50,18),steel);
 roller.rotation.z=Math.PI/2;roller.position.set(-7.8+i*1.02,.43,5.35);scene.add(roller);beltRollers.push(roller);
}
box(scene,-1.1,.94,4.45,13.8,.13,.11,steel);
box(scene,-1.1,.94,6.25,13.8,.13,.11,steel);
box(scene(5.60,.80,5.35,.48,.20,1.62,yellow));

// =========重制真实工业零件，ExtrudeGeometry拉伸法兰异形工件，缺陷件增加缺口=========
function makeMetalPart(isBad=false){
 const g=new THREE.Group();
 const aluminum=new THREE.MeshStandardMaterial({color:0xf0f3f6,metalness:0.88,roughness:0.20});
 const darkAlu=new THREE.MeshStandardMaterial({color:0xd4d9dd,metalness:0.84,roughness:0.24});
 const defectMat=new THREE.MeshStandardMaterial({color:0x999ea2,metalness:0.70,roughness:0.45});

 //法兰外形
 const shape = new THREE.Shape();
 shape.moveTo(-0.55, -0.55);
 shape.lineTo(0.55,-0.55);
 shape.lineTo(0.55,0.55);
 shape.lineTo(-0.55,0.55);
 shape.lineTo(-0.55,-0.55);
 //外圈圆角凸台
 const holePath = new THREE.Path();
 holePath.moveTo(-0.22,-0.22);
 holePath.lineTo(0.22,-0.22);
 holePath.lineTo(0.22,0.22);
 holePath.lineTo(-0.22,0.22);
 holePath.lineTo(-0.22,-0.22);
 shape.holes.push(holePath);

 const extrudeOpt = {depth:0.32,steps:2,bevelEnabled:true,bevelThickness:0.04,bevelSize:0.03};
 const flangeGeo = new THREE.ExtrudeGeometry(shape,extrudeOpt);
 const flange = new THREE.Mesh(flangeGeo, isBad ? defectMat : aluminum);
 flange.rotation.x = -Math.PI/2;
 flange.position.y = 0.22;
 flange.castShadow=true;g.add(flange);

 //中心大通孔
 const centerHole = new THREE.Mesh(new THREE.CylinderGeometry(0.14,0.14,0.40,36),darkAlu);
 centerHole.rotation.x=Math.PI/2;
 centerHole.position.y=0.22;
 g.add(centerHole);

 //轴向输出轴
 const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.11,0.11,0.62,28),aluminum);
 shaft.rotation.x=Math.PI/2;
 shaft.position.set(0,0.22,0.42);
 shaft.castShadow=true;g.add(shaft);

 //后端短轴凸台
 const rearBoss = new THREE.Mesh(new THREE.CylinderGeometry(0.13,0.13,0.38,28),aluminum);
 rearBoss.rotation.x=Math.PI/2;
 rearBoss.position.set(0,0.22,-0.36);
 rearBoss.castShadow=true;g.add(rearBoss);

 //左右侧安装耳凸台
 box(g,-0.44,0.22,0,0.22,0.34,0.26, isBad?defectMat:aluminum);
 box(g,0.44,0.22,0,0.22,0.34,0.26, isBad?defectMat:aluminum);

 //缺陷件增加缺口破损
 if(isBad){
    box(g,0.20,0.28,0.20,0.18,0.22,0.18,new THREE.MeshStandardMaterial({color:0x06121b,metalness:0,roughness:1}));
 }

 return g;
}

//工件队列
const workpieces=[];
const BASE_Y = 1.02;
const START_X = 6.2;
const STEP_X = 3.0;
for(let i=0;i<5;i++){
 const badFlag = Math.random()<SIM_CONFIG.defectRate;
 const group=makeMetalPart(badFlag);
 const initX = START_X - i * STEP_X;
 group.position.set(initX, BASE_Y, 5.35);
 scene.add(group);
 group.userData={
   index:i,
   initX: initX,
   state:'moving',
   bad:badFlag,
   missing:false,
   classified:false,
   baseY: BASE_Y
 };
 workpieces.push(group);
}

//工业相机
const cameraRig=new THREE.Group();cameraRig.position.set(-1.2,2.65,3.55);scene.add(cameraRig);
box(cameraRig,0,0,0,.86,.50,.66,dark);
const camLens=new THREE.Mesh(new THREE.CylinderGeometry(.18,.18,.36,24),mat(0x07131b,.7,.18));
camLens.rotation.x=Math.PI/2;camLens.position.set(0,0,.46);cameraRig.add(camLens);
const lensGlass=new THREE.Mesh(new THREE.CircleGeometry(.13,24),mat(0x12d8e8,.3,.15,0x087c9a));
lensGlass.position.set(0,0,.64);cameraRig.add(lensGlass);
box(scene,-1.2,1.25,3.55,.18,2.55,.18,steel);
box(scene,-1.2,2.28,3.98,.18,.16,.96,steel);
box(scene,-1.2,1.98,3.55,.76,.16,.76,dark);
const detectFrame=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(3.4,.06,1.65)),new THREE.LineBasicMaterial({color:0x14e8ee,transparent:true,opacity:0.55}));
detectFrame.position.set(-1.2,1.20,5.35);scene.add(detectFrame);
const detectBeam=new THREE.SpotLight(0x00d9e8,5.5,6,Math.PI/5,.42,1.3);detectBeam.position.set(-1.2,2.58,4.15);detectBeam.target.position.set(-1.2,1.05,5.35);scene.add(detectBeam);scene.add(detectBeam.target);

//废品箱
const rejectBin=new THREE.Group();rejectBin.position.set(-1.1,0,9.65);scene.add(rejectBin);
box(rejectBin,0,.50,0,2.4,.98,1.85,mat(0x57232a,.35,.5));
box(rejectBin,0,1.06,0,2.20,.14,1.70,mat(0xb72e36,.25,.35));
box(rejectBin,0,1.46,-.95,1.45,.78,.12,mat(0x241c25,.3,.5));
box(rejectBin,0,1.48,-.88,1.18,.50,.03,mat(0xff4545,.2,.3,0x7a1010),false);

//机械臂
function makeRobot(x,z){
 const root=new THREE.Group();root.position.set(x,0,z);scene.add(root);
 const armMat=mat(0xdce4e6,.78,.23), jointMat=mat(0x202a30,.82,.25),
       trimMat=mat(0x8d9ba0,.8,.2),rubberMat=mat(0x11191e,.25,.65);
 function cylR(parent,rt,rb,h,material,y){
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
 const base=new THREE.Mesh(new THREE.CylinderGeometry(.68,.80,.36,32),dark);
 base.position.y=.18;base.castShadow=true;root.add(base);
 cylR(root,.30,.36,1.08,armMat,.86);
 cylR(root,.35,.35,.14,jointMat,1.40);
 const shoulder=new THREE.Group();shoulder.position.set(0,1.44,0);root.add(shoulder);
 joint(shoulder,.41,.02);
 cylR(shoulder,.245,.28,1.34,armMat,.74);
 cylR(shoulder,.285,.285,.14,trimMat,.74);
 const elbow=new THREE.Group();elbow.position.set(0,1.44,0);shoulder.add(elbow);
 joint(elbow,.36,.02);
 cylR(elbow,.215,.24,1.08,armMat,.56);
 cylR(elbow,.255,.255,.12,trimMat,.56);
 const wrist=new THREE.Group();wrist.position.set(0,1.08,0);elbow.add(wrist);
 const wristJoint=new THREE.Mesh(new THREE.SphereGeometry(.27,24,18),jointMat);
 wristJoint.castShadow=true;wrist.add(wristJoint);
 const wristRing=new THREE.Mesh(new THREE.CylinderGeometry(.24,.24,.18,28),trimMat);
 wristRing.rotation.z=Math.PI/2;wrist.add(wristRing);
 box(wrist,0,-.20,.14,.36,.24,.36,armMat);
 const fingerL=box(wrist,-.18,-.46,.22,.08,.36,.14,armMat);
 const fingerR=box(wrist,.18,-.46,.22,.08,.36,.14,armMat);
 box(wrist,-.18,-.62,.22,.10,.09,.16,rubberMat);
 box(wrist,.18,-.62,.22,.10,.09,.16,rubberMat);
 cylR(shoulder,.27,.27,.08,jointMat,.24);
 cylR(elbow,.24,.24,.08,jointMat,.22);
 return {root,shoulder,elbow,wrist,fingerL,fingerR};
}
const robot=makeRobot(-1.1,7.65);

let totalDetected=0,goodDetected=0,badDetected=0,missingDetected=0,rejectStored=0,activePick=null;
function updateProductionBoard(){
 const el=id;
 el('output').textContent=(1286+totalDetected).toLocaleString('en-US');el('bottomOutput').textContent=(1286+totalDetected).toLocaleString('en-US');
 el('goodCount').textContent=1264+goodDetected;el('badCount').textContent=22+badDetected;el('missingCount').textContent=8+missingDetected;
 el('rejectBinCount').textContent=rejectStored;
 const totalAll=1286+totalDetected;
 const goodAll=1264+goodDetected;
 el('yieldRate').textContent=totalAll>0 ? (goodAll/totalAll*100).toFixed(1):"0.0";
 el('detectCount').textContent = totalDetected;
}
function logSort(message){
 const now=new Date().toLocaleTimeString();
 sortLogRecords.push({time:now,msg:message});
 if(sortLogRecords.length>150) sortLogRecords.shift();
 const el=id('sortLog');
 if(el)el.innerHTML=message+'<br>'+el.innerHTML.split('<br>').slice(0,2).join('<br>');
}
function classifyPart(part){
 if(part.userData.classified)return;
 part.userData.classified=true;totalDetected++;
 id('detectState').innerText = "已识别";
 if(part.userData.bad){
  badDetected++;
  if(part.userData.missing)missingDetected++;
  playBeepAlert();
  part.position.set(-1.1,1.12,5.35);
  part.userData.state='rejecting';part.userData.pickT=0;
  part.userData.pickStart=new THREE.Vector3(-1.1,1.12,5.35);
  activePick=part;
  logSort('<span style="color:#ff6b70">缺陷报警：工件 #'+(part.userData.index+1)+'，机械臂准备抓取</span>');
 }
 else{
  goodDetected++;part.userData.state='passed';
  logSort('<span style="color:#42e6bd">工件 #'+(part.userData.index+1)+' 检测合格，继续输送</span>');
 }
 updateProductionBoard();
}

//厂房梁柱
for(let x=-22;x<=22;x+=7.0){
 for(let z of [-16,14]){
  box(scene,x,5.5,z,.30,11,.30,steel);
 }
 box(scene,x,10.4,0,.26,.26,30,steel);
}
for(let z of [-16,14])box(scene,0,10.2,z,44,.30,.30,steel);

const lamps=[];
machines.forEach((m,i)=>{
 const l=new THREE.Mesh(new THREE.SphereGeometry(.14,14,14),new THREE.MeshBasicMaterial({color:i===machines.length-1?0xffb52e:0x13f2c1}));
 l.position.set(m.position.x,m.position.y+4.6,m.position.z);scene.add(l);lamps.push(l);
});

function animate(){
 requestAnimationFrame(animate);
 const t=performance.now()*.001 * SIM_CONFIG.speedRate;
 if(!SIM_RUNNING){
    controls.update();renderer.render(scene,camera);
    return;
 }
 if(activePick){
  const p=activePick;p.userData.pickT+=.012*SIM_CONFIG.speedRate;const q=Math.min(p.userData.pickT,1);
  const p0=p.userData.pickStart;
  const grip=new THREE.Vector3(-1.1,1.24,5.35);
  const lifted=new THREE.Vector3(-1.1,2.0,5.75);
  const carry=new THREE.Vector3(-1.1,1.95,8.65);
  const drop=new THREE.Vector3(-1.1,1.34,9.55);
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
   p.position.lerpVectors(drop,new THREE.Vector3(-1.1,1.08,9.60),k);
   robot.fingerL.position.x=-.09-.10*k;robot.fingerR.position.x=.09+.10*k;
  }
  robot.wrist.rotation.x=-.10;
  if(q>=1){
   p.visible=false;p.userData.state='stored';p.userData.storedT=0;rejectStored++;activePick=null;
   robot.shoulder.rotation.x=0;robot.elbow.rotation.x=0;robot.wrist.rotation.x=0;
   robot.fingerL.position.x=-.19;robot.fingerR.position.x=.19;
   logSort('<span style="color:#ff7777">缺陷件已投入旁侧废品箱</span>');updateProductionBoard();
  }
 }else{
  robot.shoulder.rotation.x=Math.sin(t*1.2)*.035;robot.elbow.rotation.x=.10+Math.sin(t*1.2+1)*.025;robot.wrist.rotation.x=Math.sin(t*.9)*.025;
 }
 beltRollers.forEach(roller=>{roller.rotation.x-=0.048*SIM_CONFIG.speedRate;});
 workpieces.forEach(part=>{
  if(part.userData.state==='stored'){
   part.userData.storedT=(part.userData.storedT||0)+.016*SIM_CONFIG.speedRate;
   if(part.userData.storedT>1.40){
    const isBadNew = Math.random()<SIM_CONFIG.defectRate;
    //重建工件：缺陷件直接生成带缺口版本
    const newGroup = makeMetalPart(isBadNew);
    const px = part.userData.initX;
    const py = part.userData.baseY;
    const pz = 5.35;
    newGroup.position.set(px,py,pz);
    scene.remove(part);
    const idx = workpieces.indexOf(part);
    workpieces[idx] = newGroup;
    scene.add(newGroup);
    newGroup.userData = {
        index: idx,
        initX: px,
        state:'moving',
        bad: isBadNew,
        missing: isBadNew&&Math.random()<0.5,
        classified:false,
        baseY: py
    };
   }
   return;
  }
  if(part.userData.state==='rejecting')return;
  if(part.userData.state==='queued'){
   if(!activePick){part.userData.state='moving';classifyPart(part);}
   return;
  }
  if(part.userData.state==='moving'||part.userData.state==='passed'){
   part.position.x-=0.012*SIM_CONFIG.speedRate;
   part.position.y = part.userData.baseY;
   if(!part.userData.classified&&part.position.x<=-1.1){
    if(activePick&&part.userData.bad){
      part.position.x=-1.1;
      part.userData.state='queued';
    }else if(!activePick){
      classifyPart(part);
    }else{
      part.position.x=-1.1;
    }
   }
   if(part.position.x<-7.0){
    part.position.set(part.userData.initX, part.userData.baseY, 5.35);
    part.userData.classified=false;
    part.userData.state='moving';
    part.userData.bad=Math.random()<SIM_CONFIG.defectRate;
    part.userData.missing=part.userData.bad&&Math.random()<0.5;
    part.userData.pickT=0;
    part.visible=true;
    id('detectState').innerText = "待检测";
   }
  }
 });
 detectFrame.material.opacity=.55+.45*Math.sin(t*3);
 detectBeam.intensity=4+1.5*Math.sin(t*4);
 controls.update();renderer.render(scene,camera);
}
animate();
showLoadingDone();
addEventListener('resize',()=>{
 camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();
 renderer.setSize(innerWidth,innerHeight);
});
</script>
</body>
</html>
'''
    components.html(html, height=1020, scrolling=False)


render_twin_html()
