import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;

public class RasterAlgorithmsApp extends JFrame {
    private final DrawingPanel drawingPanel;
    private Point startPoint = null;
    private final JComboBox<String> algoSel;
    private Color currColor = Color.BLUE;

    public RasterAlgorithmsApp() {
        setTitle("Raster Algorithms");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        drawingPanel = new DrawingPanel();

        algoSel = new JComboBox<>(new String[]{
                "Step Algorithm",
                "DDA Algorithm",
                "Bresenham's Line",
                "Bresenham's Circle",
                "Bresenham's Circle Filled"
        });

        JButton colorButton = new JButton("Choose Color");
        colorButton.addActionListener(e -> {
            Color selectedColor = JColorChooser.showDialog(this, "Choose Line Color", currColor);
            if (selectedColor != null) {
                currColor = selectedColor;
            }
        });

        JButton clearButton = new JButton("Clear");
        clearButton.addActionListener(e -> drawingPanel.clear());

        JTextField gridSizeField = new JTextField(5);
        JButton setGridSizeButton = new JButton("Set Grid Size");
        setGridSizeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int gridSize = Integer.parseInt(gridSizeField.getText());
                    drawingPanel.setGridSize(gridSize);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(RasterAlgorithmsApp.this, "Please enter a valid grid size.");
                }
            }
        });

        JPanel controlPanel = new JPanel();
        controlPanel.add(new JLabel("Select Algorithm:"));
        controlPanel.add(algoSel);
        controlPanel.add(colorButton);
        controlPanel.add(clearButton);
        controlPanel.add(new JLabel("Grid Size:"));
        controlPanel.add(gridSizeField);
        controlPanel.add(setGridSizeButton);

        add(controlPanel, BorderLayout.NORTH);
        add(drawingPanel, BorderLayout.CENTER);

        drawingPanel.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                startPoint = e.getPoint();
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                if (startPoint != null) {
                    Point endPoint = e.getPoint();
                    String algo = (String) algoSel.getSelectedItem();

                    Point gridStart = drawingPanel.snapToGrid(startPoint);
                    Point gridEnd = drawingPanel.snapToGrid(endPoint);

                    switch (algo) {
                        case "Step Algorithm" ->
                                drawingPanel.drawStepAlgorithm(gridStart.x, gridStart.y, gridEnd.x, gridEnd.y, currColor);
                        case "DDA Algorithm" ->
                                drawingPanel.drawDDA(gridStart.x, gridStart.y, gridEnd.x, gridEnd.y, currColor);
                        case "Bresenham's Line" ->
                                drawingPanel.drawBresenhamLine(gridStart.x, gridStart.y, gridEnd.x, gridEnd.y, currColor);
                        case "Bresenham's Circle" ->
                                drawingPanel.drawBresenhamCircle(gridStart.x, gridStart.y, gridEnd.x, gridEnd.y, currColor);
                        case "Bresenham's Circle Filled" ->
                                drawingPanel.drawBresenhamCircleFilled(gridStart.x, gridStart.y, gridEnd.x, gridEnd.y, currColor);

                    }
                    startPoint = null;
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            RasterAlgorithmsApp app = new RasterAlgorithmsApp();
            app.setVisible(true);
        });
    }
}

class DrawingPanel extends JPanel {
    private final ArrayList<Line> lines = new ArrayList<>();
    private int gridSize = 30;

    public DrawingPanel() {
        setBackground(Color.WHITE);
    }

    public void clear() {
        lines.clear();
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawGrid(g);
        for (Line line : lines) {
            g.setColor(line.color);
            for (Point point : line.points) {
                g.fillRect(point.x * gridSize, point.y * gridSize, gridSize, gridSize);
            }
        }
    }

    public void setGridSize(int size) {
        gridSize = size;
        repaint();
    }

    private void drawGrid(Graphics g) {
        g.setColor(Color.LIGHT_GRAY);
        for (int i = 0; i < getWidth(); i += gridSize) {
            g.drawLine(i, 0, i, getHeight());
        }
        for (int i = 0; i < getHeight(); i += gridSize) {
            g.drawLine(0, i, getWidth(), i);
        }

        g.setColor(Color.BLACK);
        g.fillRect(0, 0, 3, getHeight());
        g.fillRect(0, 0, getWidth(), 3);

        int maxX = getWidth() / gridSize;
        int maxY = getHeight() / gridSize;

        for (int i = 0; i <= maxX; i += 3) {
            g.drawString(String.valueOf(i), i * gridSize, 15);
        }
        for (int i = 0; i <= maxY; i += 3) {
            g.drawString(String.valueOf(i), 5, i * gridSize + 15);
        }
    }

    public Point snapToGrid(Point p) {
        int x = p.x / gridSize;
        int y = p.y / gridSize;
        return new Point(x, y);
    }

    public void drawStepAlgorithm(int x0, int y0, int x1, int y1, Color color) {
        ArrayList<Point> stepPoints = new ArrayList<>();

        int dx = x1 - x0;
        int dy = y1 - y0;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));
        float incX = (float) dx / steps;
        float incY = (float) dy / steps;
        float x = x0;
        float y = y0;
        for (int i = 0; i < steps; ++i) {
            stepPoints.add(new Point(Math.round(x), Math.round(y)));
            x += incX;
            y += incY;
        }

        lines.add(new Line(stepPoints, color));
        repaint();
    }


    public void drawDDA(int x0, int y0, int x1, int y1, Color color) {
        ArrayList<Point> points = new ArrayList<>();
        int dx = x1 - x0;
        int dy = y1 - y0;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));
        float xInc = (float) dx / steps;
        float yInc = (float) dy / steps;
        float x = x0;
        float y = y0;

        for (int i = 0; i <= steps; ++i) {
            points.add(new Point(Math.round(x), Math.round(y)));
            x += xInc;
            y += yInc;
        }
        lines.add(new Line(points, color));
        repaint();
    }

    public void drawBresenhamLine(int x0, int y0, int x1, int y1, Color color) {
        ArrayList<Point> points = new ArrayList<>();
        if (x0 < x1 && y0 < y1) {
            var tmp = x0;
            x0 = x1;
            x1 = tmp;

            tmp = y0;
            y0 = y1;
            y1 = tmp;
        }
        int dx = Math.abs(x1 - x0);
        int dy = Math.abs(y1 - y0);
        int sx = x0 < x1 ? 1 : -1;
        int sy = y0 < y1 ? 1 : -1;
        int err = dx - dy;

        while (true) {
            points.add(new Point(x0, y0));

            if (x0 == x1 && y0 == y1) {
                break;
            }

            int err2 = err * 2;
            if (err2 > -dy) {
                err -= dy;
                x0 += sx;
            }
            if (err2 < dx) {
                err += dx;
                y0 += sy;
            }
        }
        lines.add(new Line(points, color));
        repaint();
    }

    public void drawBresenhamCircle(int x0, int y0, int x1, int y1, Color color) {
        ArrayList<Point> points = new ArrayList<>();
        int radius = (int) Math.sqrt(Math.pow(x1 - x0, 2) + Math.pow(y1 - y0, 2));

        int x = 0;
        int y = radius;
        int p = 3 - 2 * radius;

        while (x <= y) {
            points.add(new Point(x0 + x, y0 + y));
            points.add(new Point(x0 - x, y0 + y));
            points.add(new Point(x0 + x, y0 - y));
            points.add(new Point(x0 - x, y0 - y));
            points.add(new Point(x0 + y, y0 + x));
            points.add(new Point(x0 - y, y0 + x));
            points.add(new Point(x0 + y, y0 - x));
            points.add(new Point(x0 - y, y0 - x));

            x++;
            if (p < 0) {
                p = p + 4 * x + 6;
            } else {
                y--;
                p = p + 4 * (x - y) + 10;
            }

        }
        lines.add(new Line(points, color));
        repaint();
    }

    public void drawBresenhamCircleFilled(int x0, int y0, int x1, int y1, Color color) {
        ArrayList<Point> points = new ArrayList<>();
        int radius = (int) Math.sqrt(Math.pow(x1 - x0, 2) + Math.pow(y1 - y0, 2));

        int x = 0;
        int y = radius;
        int p = 3 - 2 * radius;

        while (x <= y) {
            for (int i = x0 - x; i <= x0 + x; i++) {
                points.add(new Point(i, y0 + y));
                points.add(new Point(i, y0 - y));
            }
            for (int i = x0 - y; i <= x0 + y; i++) {
                points.add(new Point(i, y0 + x));
                points.add(new Point(i, y0 - x));
            }

            x++;
            if (p < 0) {
                p = p + 4 * x + 6;
            } else {
                y--;
                p = p + 4 * (x - y) + 10;
            }
        }

        lines.add(new Line(points, color));
        repaint();
    }

    private static class Line {
        ArrayList<Point> points;
        Color color;

        Line(ArrayList<Point> points, Color color) {
            this.points = points;
            this.color = color;
        }
    }
}