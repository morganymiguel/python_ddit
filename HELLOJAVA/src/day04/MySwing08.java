package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_mine = new JLabel("나:");
		lbl_mine.setBounds(64, 86, 27, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("컴:");
		lbl_com.setBounds(64, 111, 27, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_result = new JLabel("결과:");
		lbl_result.setBounds(64, 142, 27, 15);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(144, 83, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(144, 108, 116, 21);
		contentPane.add(tf_com);
		
		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(144, 139, 116, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(64, 167, 196, 23);
		contentPane.add(btn);
	}

	public void myClick() {
		
		String mine = tf_mine.getText();
		double rnd = Math.random();
		String com = "";
		String result = "";
		if(rnd >0.66) {
			com = "가위";
		}else if(rnd>0.33) {
			com = "바위";
		}else{
			com = "보";
		}
		
		if(mine.equals("가위") && com.equals("가위"))	result = "비김";
		if(mine.equals("가위") && com.equals("바위"))	result = "짐";
		if(mine.equals("가위") && com.equals("보"))	result = "이김";
		
		if(mine.equals("바위") && com.equals("가위"))	result = "이김";
		if(mine.equals("바위") && com.equals("바위"))	result = "비김";
		if(mine.equals("바위") && com.equals("보"))	result = "지짐";
		
		if(mine.equals("보") && com.equals("가위"))	result = "지짐";
		if(mine.equals("보") && com.equals("바위"))	result = "이김";
		if(mine.equals("보") && com.equals("보"))		result ="비김";
		
		tf_com.setText(com);
		tf_result.setText(result);
	}

}
