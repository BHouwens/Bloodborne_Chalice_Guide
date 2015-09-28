/* bling.js */

window.$ = document.querySelectorAll.bind(document)

Node.prototype.on = window.on = function (name, fn) {
  this.addEventListener(name, fn)
}

NodeList.prototype.__proto__ = Array.prototype

NodeList.prototype.on = NodeList.prototype.addEventListener = function (name, fn) {
  this.forEach(function (elem, i) {
    elem.on(name, fn)
  })
}

function allocateGlyphs(){
	var glyphs = $('.glyph');

	glyphs.forEach(function(el){
		var name = el.getAttribute('data-name'),
			active = document.querySelector('.active').innerHTML;

		if (name != active){
			el.classList.add('hide');
		}else{
			el.classList.remove('hide');
		}
	});
} allocateGlyphs();

$('.chalice').on('click', function(el){
	document.querySelector('.active').classList.remove('active');
	this.classList.add('active');

	allocateGlyphs();
});
