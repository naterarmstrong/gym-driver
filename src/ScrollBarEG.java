import java.awt.Color;
import java.awt.Dimension;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Paint;
import java.awt.RenderingHints;

import javax.swing.*;

public class ScrollBarEG {
    protected static final Paint GRADIENT_PAINT = new GradientPaint(0, 0,
            Color.blue, 50, 50, Color.red, true);

    private static void createAndShowGui() {
        JPanel mainPanel = new JPanel();

        JPanel canvas = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2 = (Graphics2D) g.create();
                g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                        RenderingHints.VALUE_ANTIALIAS_ON);
                g2.setPaint(GRADIENT_PAINT);
                g2.fillOval(0, 0, getWidth(), getHeight());
                g2.dispose();
            }
        };
        JScrollPane scroll = new JScrollPane();
        scroll.setViewportView(canvas);
        scroll.setPreferredSize(new Dimension(924, 700));
        canvas.setPreferredSize(new Dimension(2000, 2000));

        mainPanel.add(scroll);

        JFrame frame = new JFrame("ScrollBar Eg");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(mainPanel);
        frame.pack();
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGui();
            }
        });
    }
}
