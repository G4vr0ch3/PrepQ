(function(namespace) {
	var STEP_SPEED = 0.02;
	var JUMP_DISTANCE = 350;
	var JUMP_HEIGHT = 100;

	function Dinosaur(options) {
		this.scale = options.scale;
		this.x = options.left;
		this.y = options.bottom;
		this.draw;
		this.jumpStart = null;
	}


	Dinosaur.prototype = Object.create(GameObject.prototype);
	Dinosaur.prototype.constructor = Dinosaur;

	Dinosaur.prototype.isJumping = function(offset) {
		return this.jumpStart !== null && this.jumpDistanceRemaining(offset) > 0;
	};

	Dinosaur.prototype.jumpDistanceRemaining = function(offset) {
		if (this.jumpStart === null) return 0;
		return this.jumpStart + JUMP_DISTANCE - offset;
	};

	Dinosaur.prototype.startJump = function(offset) {
		this.jumpStart = offset;
	};

	Dinosaur.prototype.jumpHeight = function (offset) {
		var distanceRemaining = this.jumpDistanceRemaining(offset);
		if (distanceRemaining > 0) {
			var maxPoint = JUMP_DISTANCE / 2;

			if (distanceRemaining >= maxPoint) {
				distanceRemaining -= JUMP_DISTANCE
			}

			var arcPos = Math.abs(distanceRemaining / maxPoint);

			return JUMP_HEIGHT * arcPos;
		}
		return 0;
	};

	Dinosaur.prototype.draw = function(context, offset) {
		var x = this.x,
			offsetY = this.y - this.jumpHeight(offset),
			y = offsetY;

		ypos = y - 70;
		xpos = x - 5;
		dino = new Image();
		dino.src = "trex.png";
		context.drawImage(dino, xpos, ypos, 80, 80);

		context.fillStyle = 'red';

		if (this.wideEyed) {
			context.fillRect(x + 48, y - 43, 10, 3);
			context.fillRect(x + 52, y - 48, 3, 10);
		}

	};

	Dinosaur.prototype.colliders = function(offset) {
		var y = this.y - this.jumpHeight(offset);
		return [{
			x: this.x + offset,
			y: y - 20,
			width: 22,
			height: 10
		}, {
			x: this.x + offset + 12,
			y: y + 2,
			width: 10,
			height: 10
		}, {
			x: this.x + offset + 30,
			y: y - 34,
			width: 20,
			height: 10
		}];
	};


	namespace.Dinosaur = Dinosaur;
})(window);
