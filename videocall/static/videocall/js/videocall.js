$(document).ready(function () {
    $('#log-out-btn').click(function () {
        $.ajax({
            url: "/authorization/logout",
            type: "GET",
            success: function (data) {
                window.location.href = '/authorization/login/?next=/'
            }
        })
    })
})