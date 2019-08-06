// 针对log页定义一个对象
var log={
    startdate:"2019-8-5",
    enddate:"2019-9-5",
    update:"2019-8-5",
    anchor:"zstarling"
}
//由对象派生业务逻辑
log.submit={
    //验证某个值是否为空
    check:function(v){
        var _v=(v=="")?true:false;
        return _v;
    },
    autohide:function(obj){
        setTimeout(function(){
            obj.hide();
        },2000)
    }
}
//获取元素对象，并保存在变量中
// var $form=$("form");
// var $username=$("#name");
// var $password=$("#password");
// var $err1=$("#err1");
// var $err2=$("#err2");
// var $bnt=$(".btn>input");

//定义一个验证内容是否为空的函数
function checkvalue(){
    var $username=$("#name");
    var $password=$("#password");
    var $err1=$("#err1");
    var $err2=$("#err2");

        //对应$function
    // if($username.val()!=""&&$password.val()!=""){

    if ((!log.submit.check($username.val()))!=""&&(!log.submit.check($password.val()))!=""){
        return true;
    }else{
        if($username.val()==""){
            $err1.show();
            // 2秒后自动隐藏
            log.submit.autohide($err1)
            return false;
        }else{
            $err2.show();
            // 2秒后自动隐藏
            log.submit.autohide($err2) 
            return false;
        }
    }
}
// 绑定按钮的单击事件,表单提交时触发，
// $(function(){
//     $form.on("submit",function(){
//         return false;
//     })
// })

//定义一个基于列表页的业务逻辑
var lst={
    template:function(t,ul,p1,p2){
        var _html='';
                _html+='  <div class="item">';
                _html+='  <div class="title">';
                _html+='      <h3>'+t+'</h3>';
                _html+='  </div>';
                _html+='  <div class="con">';
                _html+='       <div class="cleft">';
                _html+='          <img src="'+ul+'" alt="图片不存在">';
                _html+='      </div>';
                _html+='      <div class="cright">';
                _html+='             <p class="ptop">';
                _html+='             '+p1;
                _html+='             </p>';
                _html+='             <p class="pbottom">';
                _html+='            '+p2;
                _html+='             </p>';
                _html+='       </div>';
                _html+='  </div>';
                _html+=' </div>';
                return _html;
    }
}
// 通过模板生成新的列表数据
//添加一条记录
var _HTML=lst.template('王八蛋','imgs/b.jpg','嘿 待我长发及腰嘿 归来娶我可好等你等的\
忘了笑旧了头上的金步摇啊 每一天的煎熬啊 不想别人知道默默为你 为你祈祷相信你是我的骄傲不怕辜负青春年少\
只想随你天涯海角梦里听你一声长啸忍不住想跟着你逃哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的身边就好一生\
只听你的心跳啊 每一天的煎熬啊 不想别人知道默默为你 为你祈祷相信你是我的骄傲不怕辜负青春年少只想随你天涯\
海角梦里听你一声长啸忍不住想跟着你逃哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的身边就好一生只听你的心跳不\
怕辜负青春年少只想随你天涯海角梦里听你一声长啸忍不住想跟着你逃哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的\
身边就好一生只听你的心跳一生只听你的心跳','钥玥');
// 将数据追加到列表中
$('.lst').append(_HTML);

//添加多条记录
var arrDate=[
    {
        t:'王八蛋',
        ul:'imgs/avatar.jpg',
        p1:'嘿 待我长发及腰嘿 归来娶我可好等你等的忘了笑旧了头上的金步摇啊 每一天的煎熬啊 不想别人知道默默为你 为你祈祷相信你是我的骄傲',
        p2:'钥玥'
    },
    {
        t:'王八蛋',
        ul:'imgs/e.jpg',
        p1:'不怕辜负青春年少只想随你天涯海角梦里听你一声长啸忍不住想跟着你逃哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的身边就好一生只听你的心跳啊 ',
        p2:'钥玥 '
    },
    {
        t:'王八蛋',
        ul:'imgs/v1.jpg',
        p1:'每一天的煎熬啊 不想别人知道默默为你 为你祈祷相信你是我的骄傲不怕辜负青春年少只想随你天涯海角梦里听你一声长啸忍不住想跟着你逃',
        p2:'钥玥 '
    },
    {
        t:'王八蛋',
        ul:'imgs/v2.jpg',
        p1:'哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的身边就好一生只听你的心跳不怕辜负青春年少只想随你天涯海角梦里听你一声长啸忍不住想跟着你逃',
        p2:'钥玥 '
    },
    {
        t:'王八蛋',
        ul:'imgs/zd01.jpg',
        p1:' 哪怕容颜就此苍老哪怕岁月不再逍遥赖在你的身边就好一生只听你的心跳一生只听你的心跳',
        p2:'钥玥 '
    }
]

// 使用流程
// 遍历数组，获取每一项元素对象
// 将获取的元素对象填充到样板中
// 向页面元素追加模板内容
for(var i=0;i<arrDate.length;i++){
    var _HTML=lst.template(arrDate[i].t,arrDate[i].ul,arrDate[i].p1,arrDate[i].p2);
    $(".lst").append(_HTML);
}

//定义一个基于特别推荐页的业务逻辑对象
var _imgs={
    tmpphoto:function(imgs){
        var _html="";
                _html+='     <li>';
                _html+='         <img src="'+imgs+'" alt="图片不存在">';
                _html+='     </li>';
                return _html;
    }
}
var arrImgs=[
    'imgs/b04.jpg',
    'imgs/b05.jpg',
    'imgs/banner02.jpg',
    'imgs/bi05.jpg',
    'imgs/c.jpg',
    'imgs/f.jpg',
]
for(var k=0;k<arrImgs.length;k++){
    var _HTML=_imgs.tmpphoto(arrImgs[k]);
    $(".body>.ad>.imglst>ul").append(_HTML);
}

//定义一个基于我的相册页的业务逻辑对象
var pics={
    template:function(ul,num,title){
    var _html='';
            _html+='<div class="item">';
            _html+='<div class="imgs">';
            _html+='   <img src="'+ul+'" alt="图片不存在">';
            _html+='   <div class="tip">喜欢 | '+num+'</div>';
            _html+='</div>';
            _html+='<div class="title">';
            _html+='  <h3>'+title+'</h3>';
            _html+='</div>';
            _html+='</div>';
            return _html;
    }
}
var arrpics=[
    { 
       ul:'imgs/toppic02.jpg',
       num:123,
       title:'王八蛋',
    },
    {
        ul:'imgs/banner01.jpg',
        num:456,
        title:'王八蛋',
    },
    {
        ul:'imgs/a.jpg',
        num:789,
        title:'王八蛋',
    },
]
for(var j=0;j<arrpics.length;j++){
    var _HTML=pics.template(arrpics[j].ul,arrpics[j].num,arrpics[j].title);
    $("#pics").append(_HTML);
}