package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Component;
import java.awt.ComponentOrientation;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 283, 347);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수:");
		lbl.setComponentOrientation(ComponentOrientation.RIGHT_TO_LEFT);
		lbl.setBounds(23, 40, 92, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setComponentOrientation(ComponentOrientation.RIGHT_TO_LEFT);
		tf.setBounds(127, 37, 107, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
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
		btn.setBounds(23, 86, 211, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setComponentOrientation(ComponentOrientation.LEFT_TO_RIGHT);
		ta.setBounds(23, 130, 211, 168);
		contentPane.add(ta);
		
	}
	
	 public void myClick() { // TODO Auto-generated method stub
		 String sdan=tf.getText();
		 int dan = Integer.parseInt(sdan);
		 
		 String txt ="";
		 txt += dan +"*" + 1 +"= "+dan*1+"\n";
		 txt += dan +"*" + 2 +"= "+dan*2+"\n";
		 txt += dan +"*" + 3 +"= "+dan*3+"\n";
		 txt += dan +"*" + 4 +"= "+dan*4+"\n";
		 txt += dan +"*" + 5 +"= "+dan*5+"\n";
		 
		 txt += dan +"*" + 6 +"= "+dan*6+"\n";
		 txt += dan +"*" + 7 +"= "+dan*7+"\n";
		 txt += dan +"*" + 8 +"= "+dan*8+"\n";
		 txt += dan +"*" + 9 +"= "+dan*9+"\n";
		 
		 ta.setText(txt);
		
		 
	 }
	
}
