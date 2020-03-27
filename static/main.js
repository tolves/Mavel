$(document).ready(function () {

    $(function () {
        $('.panel').css({'height': $(window).height()});
        $.scrollify({
            // section: '.panel',
            section: '#panel',
            // sectionName : "section-name",
            scrollbars: true,
            // interstitialSection : "",
            easing: "easeOutExpo",
            scrollSpeed: 1000,
            offset: 0,
            standardScrollElements: "",
            setHeights: true,
            overflowScroll: true,
            updateHash: true,
            touchScroll: true,
            before: function () {
            },
            after: function () {
            },
            afterResize: function () {
            },
            afterRender: function () {
            }
        });
    });

    var mySwiper = new Swiper ('.swiper-container', {
        direction: 'horizontal', // 垂直切换选项
        loop: false, // 循环模式选项

        // 如果需要前进后退按钮
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        slidesPerView: 5,
        spaceBetween: 80,
        setWrapperSize: true,
        autoHeight: true,
        preloadImages: false,
        slidesOffsetBefore: 50,
        // spaceBetween: '100px',
    });


    showPjDesc = function(id){
        $.get("ajax_project/"+id,function(result){
            inhtml ="<div style='background: url("+result['bgimage']+"); height: 100%; background-size: cover;'>"+
                    "<a href='#2' onclick='closePjDesc();' style='margin-left: 95%'>关闭</a>"+
                    "<div class='sub-content' style='display: none'>"+
                    "<p>项目名"+result['name']+"</p>"+
                    "<p>项目简介"+result['desc']+"</p>"+
                    "<p>作者"+result['author']+"</p>"+
                    "<p>链接"+result['link']+"</p>"+
                    "</div></div>";
            $('#pjdesc').html(inhtml);
            $(".sub-content").fadeIn(1000);
        })

        $("#pjdesc").show();
    }

    closePjDesc = function(){
        $("#pjdesc").hide();
    }

});

$(document).mouseup(function(e) {
    var  pop = $("#pjdesc");
    if(!pop.is(e.target) && pop.has(e.target).length === 0) {
        $("#pjdesc").hide();
    }
});