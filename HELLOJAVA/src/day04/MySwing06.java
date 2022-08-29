package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.text.BadLocationException;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Arrays;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn_call;
	JButton btn0;
	JButton btn1;
	JButton btn2;
	JButton btn3;
	JButton btn4;
	JButton btn5;
	JButton btn6;
	JButton btn7;
	JButton btn8;
	JButton btn9;
	String txt="";
	int cnt = 0;
	
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(12, 23, 177, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn1.getText());
				myClick(num);
			}
		});
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn1.setBounds(12, 62, 47, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn2.getText());
				myClick(num);

			}
		});
		btn2.setBounds(81, 62, 47, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn3.getText());
				myClick(num);

			}
		});
		btn3.setBounds(142, 62, 47, 23);
		contentPane.add(btn3);
		
		btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn6.getText());
				myClick(num);

			}
		});
		btn6.setBounds(142, 111, 47, 23);
		contentPane.add(btn6);
		
		btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn5.getText());
				myClick(num);

			}
		});
		btn5.setBounds(81, 111, 47, 23);
		contentPane.add(btn5);
		
		btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn4.getText());
				myClick(num);

			}
		});
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
			}
		});
		btn4.setBounds(12, 111, 47, 23);
		contentPane.add(btn4);
		
		btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn7.getText());
				
				myClick(num);

			}
		});
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn7.setBounds(12, 156, 47, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn8.getText());
				myClick(num);

			}
		});
		btn8.setBounds(81, 156, 47, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn9.getText());
				myClick(num);

			}
		});
		btn9.setBounds(142, 156, 47, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num = Integer.parseInt(btn0.getText());
				
				myClick(num);
			}
		});
		btn0.setBounds(12, 201, 47, 23);
		contentPane.add(btn0);
		
		btn_call = new JButton("call");
		btn_call.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				myClick();
			}
		});
		btn_call.setBounds(81, 201, 108, 23);
		contentPane.add(btn_call);
	}
	
	public void myClick(int num) {
		cnt++;
		if(cnt<=11) {
			txt+=num;
			tf.setText(txt);
			
		}else {
			JOptionPane.showMessageDialog(null, "번호입력 초과");
		}
		
		
	}
	

	public void myClick() {
		
		JOptionPane.showMessageDialog(null, txt);
		
	}

}
