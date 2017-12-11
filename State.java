package hw4;

public class State {
	double ballX;
	double ballY;
	double velocityX;
	double velocityY;
	double paddleY;
	
	public State(double ballX, double ballY, double velocityX, double velocityY, double paddleY){
		this.ballX = ballX;
		this.ballY = ballY;
		this.velocityX = velocityX;
		this.velocityY = velocityY;
		this.paddleY = paddleY;
	}
	
}
