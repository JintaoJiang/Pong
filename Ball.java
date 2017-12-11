import java.util.Random;

public class Ball {

	private double x, y, vx, vy;

	public Ball(){
		this.x = 0.5;
		this.y = 0.5;
		this.vx = 0.03;
		this.vy = 0.01;
	}

	public void bounce(){
		if(this.y < 0){
			this.y *= -1;
			this.vy *= -1;
		}
		else if(this.y > 1){
			this.y = 2 - this.y;
			this.vy *= -1;
		}
		else if(this.x < 0){
			this.x *= -1;
			this.vx *= -1;
		}
	}

	public void bounce_paddle(){
		this.x = 2 - this.x;
		double U = Math.random() * 0.03 - 0.015;
		double V = Math.random() * 0.06 - 0.03;
		this.vx = -this.vx + U;
		this.vy += V;
		if(vx > 0){
			vx = Math.max(0.03, vx);
		}
		else
			vx = Math.min(-0.03, vx);
	}

	public void update(){
		this.x += this.vx;
		this.y += this.vy;
		this.bounce();
	}


}