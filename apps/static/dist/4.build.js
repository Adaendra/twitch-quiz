(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{13:function(t,e,s){var i=s(14);"string"==typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);(0,s(5).default)("02cd9fce",i,!0,{})},14:function(t,e,s){(t.exports=s(4)(!1)).push([t.i,".clock{color:#c03763;font-size:48px;line-height:1.1em;margin:40px 0 60px}",""])},16:function(t,e,s){"use strict";var i={data:()=>({time:"00:00:00"}),mounted(){this.startTime()},methods:{startTime(){let t=new Date,e=t.getHours(),s=t.getMinutes(),i=t.getSeconds();s=this.checkTime(s),i=this.checkTime(i),this.time=e+":"+s+":"+i;setTimeout(this.startTime,500)},checkTime:t=>(t<10&&(t="0"+t),t)}},c=s(3);var n=function(t){s(13)},o=Object(c.a)(i,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"clock"},[e("h1",[this._v(this._s(this.time))])])}),[],!1,n,null,null);e.a=o.exports},63:function(t,e,s){var i=s(64);"string"==typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);(0,s(5).default)("8cdad0d8",i,!0,{})},64:function(t,e,s){(t.exports=s(4)(!1)).push([t.i,"",""])},67:function(t,e,s){"use strict";s.r(e);var i={data:()=>({msg:"TEST"}),components:{Clock:s(16).a}},c=s(3);var n=function(t){s(63)},o=Object(c.a)(i,(function(){var t=this.$createElement;return(this._self._c||t)("h1",[this._v(this._s(this.msg))])}),[],!1,n,null,null);e.default=o.exports}}]);