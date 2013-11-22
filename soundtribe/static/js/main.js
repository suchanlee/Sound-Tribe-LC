$(function($) {
	// setHeaderTop();
	setThreadWidthHeight();
	setSplashElemDim();
	setSubscriptionVar(false);
	$('.thread-anchors').addClass('anchor');
});

$(window).resize(function() {
	setThreadWidthHeight();
	setSplashElemDim();
});

$(window).scroll(function() {
	var pos = $('body').scrollTop();
	if (pos%20 === 0) {
		updateThreadPath(pos);
	}
});

function setSplashElemDim() {
	var recents = $('.splash-recent-list');
	recents.height(recents.width());
	var interview1 = $('#splash-interviews-1');
	var interview_container = $('#splash-interviews-2-container');
	var interview2 = $('#splash-interviews-2');
	var interview3 = $('#splash-interviews-3');
	interview1.height(interview1.width());
	interview_container.height(interview1.width());
	interview2.height(interview2.width()/2.12);
	interview3.height(interview3.width()/2.12);
	// var header_nav = $('#header-nav');
	// header_nav.width($('#container').width()*0.86-$('#header-logo img').width()-3);
	var category_image = $('.category-item-image');
	var category_info = $('.category-item-info');
	category_image.height(category_image.width());
	category_info.width($('.category-item').width()-category_image.width()-90);
}

function setSubscriptionVar(val) {
	window.subscription = val;
}

function getSubscriptionVar() {
	return window.subscription;
}

function updateThreadPath(position) {
	var cur_position = position;
	var anchors = $('.thread-anchors');
	var len = anchors.length;
	var anchor;
	for (var i=0; i<len; i++) {
		anchor = $(anchors[len-i-1]);
		if (anchor.offset().top < cur_position) {
			var link = anchor.attr('href');
			if (window.location.pathname !== link) {
				history.replaceState('', '', link);
				document.title = anchor.attr('title');
				if (getSubscriptionVar()) {
					$('.thread-subscribe').css('display','none');
				}
			}
			break;
		}
	}
}

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

$('#nav-bar-toggle').click(function() {
	$('#header-nav').slideToggle();
});

$('.subscribe-submit').click(function() {
	var email = $(this).siblings('input[type="email"]').val();
	var csrf = $('#csrf-token').text();
	var subscribe = $(this);
	if (validateEmail(email)) {
		$.ajax({
			type: "POST",
			url: "/subscribe/submit/",
			data: {
				email: email,
				csrfmiddlewaretoken: csrf,
			},
			success: function(data) {
				subscribe.siblings('.subscribe-error').css('display', 'none');
				subscribe.siblings('input[type="email"]').css('display', 'none');
				subscribe.css('display', 'none');
				subscribe.siblings('.subscribe-success').fadeIn();
				$('#subscribe-text').css('display', 'none');
				$('#subscribe-email').css('display','none');
				setSubscriptionVar(true);
			},
			error: function(data) {
				subscribe.siblings('.subscribe-error').val('There was an error. Please try again.').fadeIn('display', 'block');
			}
		});
	} else {
		$(this).siblings('.subscribe-error').fadeIn();
	}
	return false;
});

$('.fold-unfold-anchor').click(function() {
	$('.fold-unfold').toggle();
});

$('#icon-search').click(function() {
	$('#header-search').toggle();
});

$('.header-menu-submenu-anchor').hover(function() {
	$('.header-menu-submenu').css('display','none');
	var submenu = $(this).children()[1];
	$(submenu).css('display','block');
});

$('#threads2').hover(function() {
	$('.header-menu-submenu').css('display','none');
});

$('#header-pull img').click(function() {
	headerToggle();
});

$('#header-logo').click(function() {
	headerToggle();
});

$('.thread-img').mouseover(function() {
	$(this).css('-webkit-filter','none');
});

$('.thread-img').mouseout(function() {
	$(this).css('-webkit-filter','saturate(50%)');
});

$('.thread-text').mouseover(function() {
	$($(this).siblings()[0]).css('-webkit-filter', 'none');
});

$('.thread-text').mouseout(function() {
	$($(this).siblings()[0]).css('-webkit-filter', 'saturate(50%)');
});

$('body').on('click', 'a.thread-like-button', function() {
	if (!$(this).hasClass('thread-liked')) {
		$(this).css('color','#A00000');
		$.ajax({
			url: window.location.pathname + 'likes/',
			method: "POST",
			data: {
				csrfmiddlewaretoken: $('#csrf_token').text(),
			},
			success: function(data) {
				console.log(data);
			},
			error: function() {
				console.log('error');
			}
		});
		$(this).addClass('thread-liked');
		$(this).attr('title', parseInt($(this).attr('rel'))+1 +' likes');
		$(this).siblings('.thread-social-like-thanks').css('display', 'block');
	} else {
		console.log('you have already liked this thread');
	}
});


$('#thread-menu').hover(function() {
	if ($(this).hasClass('low-menu-animated')) {
		$(this).removeClass('low-menu-animated');
	}
	$(this).animate({
		'opacity': '1.0',
	}, 'fast');
});


function setThreadWidthHeight() {
	var thread_square = $('.thread-square');
	var thread_overlay = $('.thread-square-overlay');
	var winW = $('#container').width();
	thread_square.height(winW/4);
	thread_square.width(winW/4);
	thread_overlay.height(winW/12);
	$('.thread-text').height(winW/12);
}

function headerToggle() {
	var header = $('header');
	var navH = $('nav').height();
	var sign = '+=';
	if (header.css('top') == '0px') {
		sign = '-=';
		$('#header-pull img').attr('src', 'static/img/arrow-03.png');
	} else {
		$('#header-pull img').attr('src', 'static/img/arrow-03-up.png');
	}
	header.animate({
		'top': sign + navH,
	}, 'slow');
}

$(window).scroll(function() {
	var scrollTop = $(this).scrollTop();
	var menu = $('#thread-menu');
	if (scrollTop > 80 && !menu.hasClass('low-menu-animated')) {
		menu.removeClass('high-menu-animated');
		menu.addClass('low-menu-animated');
		menu.animate({
			'opacity': '0.2',
		}, 'fast');
	}
	if (scrollTop <= 80 && !menu.hasClass('high-menu-animated')) {
		menu.removeClass('low-menu-animated');
		menu.addClass('high-menu-animated');
		$('#thread-menu').animate({
			'opacity': '1.0',
		}, 'fast');
	}
});
