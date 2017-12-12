public class Paddle {
	private double paddle_height = 0.2;
	private double x, y, v;

	public Paddle(){
		x = 1.0;
		y = 0.5 - height / 2;
		v = 0.04;
	}

	public void check(){
		y = Math.max(0, y);
		y = Math.min(0.8, y);
	}

	public void qlearn(){

	}

	
}