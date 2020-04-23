$(document).ready(function(){
	
	$("#cancel").click(function(){
		location.href = "/list.py";
	});
	
	$("#write").click(function(){
		
		var params = {};
		params.title = $("#title").val();
		params.content = $("#content").val();
		
		if(params.title == "") {
			alert("제목이 필요합니다.");
			return;
		}
		
		$.ajax({
			type: "get",
			url: "/writeForm.py",
			data: params
		}).done(function(d) {
			console.log(d);
			if(d == 1) {
				location.href = "/list.py";
			} else {
				alert("작성 중 오류 발생!");
			}
		});
		
	});
	
});