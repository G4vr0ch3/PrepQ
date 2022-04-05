(function(namespace) {
	function Cactus(options) {
		this.scale = options.scale;
		this.x = options.left;
		this.y = options.bottom;
		this.colour = options.colour;
		this.leftSize = options.leftSize;
		this.centerSize = options.centerSize;
		this.rightSize = options.rightSize;
	}

	Cactus.prototype = Object.create(GameObject.prototype);
	Cactus.prototype.constructor = Cactus;

	Cactus.prototype.draw = function(context, offset) {
		var x = this.x - offset,
			y = this.y,
			scale = this.scale;
		image = new Image()
		image.src = "ursin.png"
		size = this.scale * 60
		context.drawImage(image, x, y - size, size, size)
	};

	Cactus.prototype.colliders = function(offset) {
		return [{
			x: this.x + this.scale * 15,
			y: this.y - this.scale * 15,
			width: 30 * this.scale,
			height: 30  * this.scale
		}];
	};

	namespace.Cactus = Cactus;
})(window);
