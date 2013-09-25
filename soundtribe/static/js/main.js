$(function($) {
	setHeaderTop();
	setThreadWidthHeight();
	$('.thread-anchors').addClass('anchor');
});

$(window).resize(function() {
	setThreadWidthHeight();
	updateThreadPath();
});

function setHeaderTop() {
	var header = $('header');
	var nav = $('nav');
	header.css('top', nav.height()*-1);
}

function updateThreadPath() {
	var url = 'somenewurl';
	history.pushState('', 'New page title', url);
}

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
			success: function() {
				console.log('success');
			},
			error: function() {
				console.log('error');
			}
		});
		$(this).addClass('thread-liked');
		$(this).attr('title', parseInt($(this).attr('rel'))+1 +' likes');
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
