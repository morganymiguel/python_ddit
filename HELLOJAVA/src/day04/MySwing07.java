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
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JButton btn;
	JTextArea ta;
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
		setBounds(100, 100, 255, 343);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수:");
		lbl.setBounds(25, 24, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(112, 21, 66, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(23, 52, 155, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(25, 85, 155, 184);
		contentPane.add(ta);
	}
	
	public void myclick() {
		String dan = tf.getText();
		int idan = Integer.parseInt(dan);
		
		String txt = "";
		txt += idan+"*"+1+"="+(idan*1)+"\n";
		txt += idan+"*"+2+"="+(idan*2)+"\n";
		txt += idan+"*"+3+"="+(idan*3)+"\n";
		txt += idan+"*"+4+"="+(idan*4)+"\n";
		txt += idan+"*"+5+"="+(idan*5)+"\n";
		
		txt += idan+"*"+6+"="+(idan*6)+"\n";
		txt += idan+"*"+7+"="+(idan*7)+"\n";
		txt += idan+"*"+8+"="+(idan*8)+"\n";
		txt += idan+"*"+9+"="+(idan*9)+"\n";
		
		
		ta.setText(txt);
		
	}
	
}












