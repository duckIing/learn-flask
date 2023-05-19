;
var member_reg_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".reg_wrap .do-reg").click(function () {

            var btn_target = $(this);

            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理！！请不要重复点击~~");
                return;
            }

            var nick_name = $(".reg_wrap input[name=nick_name]").val();
            var login_name = $(".reg_wrap input[name=login_name]").val();
            var login_pwd1 = $(".reg_wrap input[name=login_pwd1]").val();
            var login_pwd2 = $(".reg_wrap input[name=login_pwd2]").val();

            if (nick_name === undefined || nick_name.length < 2) {
                common_ops.alert("请输入正确的昵称~~");
                return;
            }

            if (login_name === undefined || login_name.length < 2) {
                common_ops.alert("请输入正确的登录用户名~~");
                return;
            }

            if (login_pwd1 === undefined || login_pwd1.length < 6) {
                common_ops.alert("请输入正确的登录密码，并且不能小于6个字符~~");
                return;
            }

            if (login_pwd2 === undefined || login_pwd2 !== login_pwd1) {
                common_ops.alert("请输入正确的确认登录密码~~");
                return;
            }

            btn_target.addClass("disabled");

            $.ajax({
                url: common_ops.buildUrl("/reg/check"),
                type: "POST",
                data: {
                    nick_name: nick_name,
                    login_name: login_name,
                    login_pwd1: login_pwd1,
                    login_pwd2: login_pwd2,
                },
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code === 200) {
                        callback = function () {
                            window.location.href = common_ops.buildUrl("/login/");
                        };
                    }
                    common_ops.alert(res.msg, callback);
                }
            });

        });
    }
};

$(document).ready(function () {
    member_reg_ops.init();
});