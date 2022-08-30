package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing10 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	JTextArea ta;
	int[] com_arr = new int[3];
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing10 frame = new MySwing10();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing10() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 251, 312);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("까꿍");
		lbl.setBounds(24, 35, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(93, 32, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(24, 60, 185, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(24, 93, 185, 158);
		contentPane.add(ta);
		setComArr();
	}

	
	public void myClick() {
		
	}
	public void myclick() {
		String mine = tf.getText();
		int[] mine_arr = new int[3];
		mine_arr[0] = Integer.parseInt(mine.substring(0,1));
		mine_arr[1] = Integer.parseInt(mine.substring(1,2));
		mine_arr[2] = Integer.parseInt(mine.substring(2,3));
		
		int strike = getStrike(com_arr,mine_arr);
		int ball= getBall(com_arr,mine_arr);
		
		String str_line = mine +"-"+strike+"S"+ball+"B\n";
		String str_old = ta.getText();
		
		ta.setText(str_old + str_line);
		tf.setText("");
		
		if(strike == 3) {
			JOptionPane.showMessageDialog(this,"당신이 이겼습니다.");
		}
	}
	
	public int getStrike(int[]com_arr, int[]mine_arr) {
		int cnt = 0;
		if(com_arr[0] == mine_arr[0])cnt++;
		if(com_arr[1] == mine_arr[1])cnt++;
		if(com_arr[2] == mine_arr[2])cnt++;
		return cnt;
	}
	public int getBall(int[]com_arr, int[]mine_arr) {
		int cnt = 0;
		if(com_arr[0] == mine_arr[1] || com_arr[0] == mine_arr[2])cnt++;
		if(com_arr[1] == mine_arr[0] || com_arr[1] == mine_arr[2])cnt++;
		if(com_arr[2] == mine_arr[0] || com_arr[2] == mine_arr[1])cnt++;
		return cnt;
	}
	public void setComArr() {
		int[] arr9 = {1,2,3,4,5,6,7,8,9};
		for(int i = 0; i<1000; i++) {
			int idx= (int)(Math.random()*9);
			int a = arr9[idx];
			int b = arr9[0];
			arr9[0] = a;
			arr9[idx] = b;
		}
		com_arr[0] = arr9[0];
		com_arr[1] = arr9[1];
		com_arr[2] = arr9[2];
		System.out.println(com_arr[0]+" "+com_arr[1]+" "+com_arr[2]+" ");
	}

}
