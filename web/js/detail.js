$(document).ready(function(){
	var getParam = function(){
		var q = document.location.search;
		var params = q.substring(1, q.length);
		var paramArr = params.split("&");
		var param = paramArr[0].split("=");
		var p = {}; 
		p[param[0]] = param[1];
		return p;
	}
	
	$.ajax({
		type: "get",
		url: "/detailData.py",
		data: getParam()
	}).done(function(d) {
		$(".title").text(d.title);
		$(".content").text(d.content);
		$("#content").val(d.content);
	});
	
	$("#btn1").click(function(){
		location.href = "/list.py";
	});
	
	$("#btn2").click(function(){
		location.href = "/delete.py?num=" + getParam().num;
	});
	
	$("#btn3").click(function(){
		$(".buttons").removeClass("disNone");
		$(".buttons").eq(1).addClass("disNone");
		$(".content").addClass("disNone");
		$("form").removeClass("disNone");
	});
	
	$("#btn4").click(function(){
		$(".buttons").removeClass("disNone");
		$(".buttons").eq(0).addClass("disNone");
		$(".content").removeClass("disNone");
		$("form").addClass("disNone");
		
		var content = $(".content").text();
		$("#content").val(content);
	});
	
	$("#btn5").click(function(){
		var params = getParam();
		params.content = $("#content").val();
		$.ajax({
			type: "get",
			url: "/updateForm.py",
			data: params
		}).done(function(d) {
			if(d == 1) {
				$(".buttons").removeClass("disNone");
				$(".buttons").eq(0).addClass("disNone");
				$(".content").removeClass("disNone");
				$("form").addClass("disNone");
				
				var content = $("#content").val();
				$(".content").text(content);
			}
		});
	});
});