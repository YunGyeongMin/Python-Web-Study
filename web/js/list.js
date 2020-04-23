$(document).ready(function(){
	console.log(1);
	$.ajax({
		type: "get",
		url: "/resource.py"
	}).done(function(d) {
		console.log(d)
		for(var row in d) {
			var html = `
					<li class="row">
						<div class="col1">${d[row].no}</div>
						<div class="col2">${d[row].title}</div>
					</li>	
			`;
			$(".body").append(html);
		}
		event();
	});
	console.log(2);
	var event = function(){
		$(".body li").click(function(){
			// console.log("111", $(this).find(".col1").text());
			var num = $(this).find(".col1").text();
			location.href = "/detail.py?num=" + num;
		});
	}
	
});