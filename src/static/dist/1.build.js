(window.webpackJsonp=window.webpackJsonp||[]).push([[1],[,,,,,,,,,,,,function(t,e,s){var i=s(13);"string"==typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);(0,s(5).default)("02cd9fce",i,!0,{})},function(t,e,s){(t.exports=s(4)(!1)).push([t.i,".clock{color:#c03763;font-size:48px;line-height:1.1em;margin:40px 0 60px}",""])},function(t,e,s){"use strict";var i={data:()=>({time:"00:00:00"}),mounted(){this.startTime()},methods:{startTime(){let t=new Date,e=t.getHours(),s=t.getMinutes(),i=t.getSeconds();s=this.checkTime(s),i=this.checkTime(i),this.time=e+":"+s+":"+i;setTimeout(this.startTime,500)},checkTime:t=>(t<10&&(t="0"+t),t)}},n=s(3);var c=function(t){s(12)},o=Object(n.a)(i,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"clock"},[e("h1",[this._v(this._s(this.time))])])}),[],!1,c,null,null);e.a=o.exports},function(t,e,s){var i=s(16);"string"==typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);(0,s(5).default)("75b56f98",i,!0,{})},function(t,e,s){(t.exports=s(4)(!1)).push([t.i,"",""])},,,,,function(t,e,s){"use strict";s.r(e);var i={data:()=>({msg:"Home"}),components:{Clock:s(14).a}},n=s(3);var c=function(t){s(15)},o=Object(n.a)(i,(function(){var t=this.$createElement;return(this._self._c||t)("h1",[this._v(this._s(this.msg))])}),[],!1,c,null,null);e.default=o.exports}]]);