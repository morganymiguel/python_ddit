package day03;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		
		System.out.println(hum.flagMove);
		System.out.println(hum.skill_tool);
		hum.die();
		hum.momstouch(10);
		System.out.println(hum.flagMove);
		System.out.println(hum.skill_tool);
		
	}
}
