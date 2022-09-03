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

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 225, 336);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수");
		lbl_first.setBounds(34, 30, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수");
		lbl_last.setBounds(34, 66, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(122, 27, 50, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setBounds(122, 63, 50, 21);
		contentPane.add(tf_last);
		tf_last.setColumns(10);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
				
			}
		});
		btn.setBounds(34, 91, 141, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(34, 124, 141, 146);
		contentPane.add(ta);
	}
	
	
	public String drawStar(int cnt) {
		String ret = "";
		for(int i=0;i<cnt;i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
		
	}
	
	public void myclick(){
		String f = tf_first.getText();
		String l = tf_last.getText();
		int ff = Integer.parseInt(f);
		int ll = Integer.parseInt(l);
		
		
		String txt = "";
		for(int i=ff;i<=ll;i++) {
			txt += drawStar(i);
		}
		
		ta.setText(txt);
		
	}

}




















