function scrollFunctionabout(){
    var x = 0 ;
    var id = setInterval(frame,15);
    function frame(){
        if(x>=720){
            clearInterval(id);
        }
        else{
            window.scrollTo(0,x);
            x=x+50;
        }
    }
}
function  scrollFunctionevents(){
    var x =0;
    var id = setInterval(frame,15);
    function frame(){
        if(x>=2160){
            clearInterval(id);
        }
        else{
            window.scrollTo(0,x);
            x=x+50;
        }
    }
}
function scrollFunctionhome(){
    window.scrollTo(0,0);
}

window.onscroll = function(event) {
    if (document.documentElement.scrollTop > 360 || document.body.scrollTop > 360) {
        $('#left').hide(1000);
        $('#centre').hide(1000);
        $('#reg').hide(1000);
        $('#events').hide(1000);
        $('#menu').show(1000);
    }
    else {
        $('#left').show(1000);
        $('#centre').show(1000);
        $('#reg').show(1000);
        $('#events').show(1000);
        $('#close').hide();
        $('#menu').hide(1000);
    }

        $('#univ-container').css('opacity','1');
    $('.about-extropy').css('opacity','1');
    $('.section_1_wrap').css('opacity','1');
    $('.section_3').css('opacity','1');
    $('.team-cont').css('opacity','1');
}
$('#menu').click(function () {
    $('#univ-container').css('opacity','0.2');
    $('.about-extropy').css('opacity','0.2');
    $('.section_1_wrap').css('opacity','0.2');
    $('.section_3').css('opacity','0.2');
    $('.team-cont').css('opacity','0.2');
    $('#left').show(1000);
        $('#centre').show(1000);
        $('#reg').show(1000);
        $('#events').show(1000);
        $('#menu').hide(1000);
        $('#close').show(1000);
});
$('#close').click(function () {
    $('#close').hide(1000);
    $('#left').hide(1000);
        $('#centre').hide(1000);
        $('#reg').hide(1000);
        $('#events').hide(1000);
        $('#menu').show(1000);
        $('#univ-container').css('opacity','1');
    $('.about-extropy').css('opacity','1');
    $('.section_1_wrap').css('opacity','1');
    $('.section_3').css('opacity','1');
    $('.team-cont').css('opacity','1');
});