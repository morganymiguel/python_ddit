package day03;

public class OopTest {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.flagMove);
		ani.die();
		System.out.println(ani.flagMove);
		
		Human hum = new Human();
		System.out.println(hum.flagMove);
		System.out.println(hum.skil_tool);
		hum.die();
		hum.momstouch(10);
		System.out.println(hum.flagMove);
		System.out.println(hum.skil_tool);
	}
}
