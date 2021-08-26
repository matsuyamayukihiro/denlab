/*
$(document).ready(function () {
  $('.slick02').slick({
    responsive: [{
        breakpoint: 768,
        settings: {
          arrows: false,
        }
      },
      {
        breakpoint: 640,
        settings: {
          arrows: false,
          dots: false,
        }
      },
    ]
  });
});
*/

$(document).on('ready', function() {
  $(".regular").slick({
    autoplay: true,
    autoplaySpeed: 4000,
    dots: true,
  });
});

/*
$('.slick01').slick({
  responsive: [{
      breakpoint: 768,
      settings: {
        arrows: false,
      }
    },
    {
      breakpoint: 640,
      settings: {
        arrows: false,
        dots: false,
      }
    },
  ]
});

$('.slick03').slick({
  autoplay:true,
  autoplaySpeed:5000,
  dots:true,
});


$('.fade').slick({
  dots: true,
  infinite: true,
  speed: 500,
  fade: true,
  cssEase: 'linear'
});
*/