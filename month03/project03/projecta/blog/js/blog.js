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
            obj.hide()
        },2000)
    }
}
//获取元素对象，并保存在变量中
var $form=$("form");
// var $username=$("#name");
// var $password=$("#password");
// var $err1=$("#err1");
// var $err2=$("#err2");
var $bnt=$(".btn>input");

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