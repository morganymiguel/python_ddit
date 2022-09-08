package day11;

public class MyThreadTest2 {
	public static void printNum() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i = 1; i<10000000;i++) {
					System.out.print(i);
					if(i%100 == 0) {
						System.out.println();
					}
				}
			}
			
		}).start();
	}
	private static void printAscii() {
		new Thread(new Runnable() {
			@Override
			public void run() {
				for(int i = 1; i<10000000; i++) {
					System.out.print((char)i);
					if(i %100 ==0 ) {
						System.out.println();
					}
					
				}
			}
			
		}).start();
			}
	public static void main(String[] args) {
		printNum();
		printAscii();
	}

}
