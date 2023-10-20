import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SpaceInvadersGame extends JPanel implements KeyListener, ActionListener {
    private int playerX, playerY;
    private List<Alien> aliens;
    private List<Bullet> bullets;
    private boolean isGameOver;
    private int score;

    private SpaceInvadersGame() {
        playerX = 300;
        playerY = 480;
        isGameOver = false;
        score = 0;

        aliens = new ArrayList<>();
        bullets = new ArrayList();

        // Initialize aliens
        for (int i = 0; i < 6; i++) {
            aliens.add(new Alien(i * 100, 0));
        }

        Timer timer = new Timer(15, this);
        timer.start();

        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Draw background
        g.setColor(Color.black);
        g.fillRect(0, 0, 800, 600);

        // Draw player
        g.setColor(Color.blue);
        g.fillRect(playerX, playerY, 50, 50);

        // Draw aliens
        for (Alien alien : aliens) {
            g.setColor(Color.green);
            g.fillRect(alien.x, alien.y, 50, 50);
        }

        // Draw bullets
        for (Bullet bullet : bullets) {
            g.setColor(Color.red);
            g.fillRect(bullet.x, bullet.y, 10, 20);
        }

        // Display score
        g.setColor(Color.white);
        g.setFont(new Font("Arial", Font.PLAIN, 20));
        g.drawString("Score: " + score, 10, 30);

        if (isGameOver) {
            g.setFont(new Font("Arial", Font.PLAIN, 50));
            g.drawString("Game Over", 300, 300);
        }
    }

    public void actionPerformed(ActionEvent e) {
        if (!isGameOver) {
            // Move aliens
            for (Alien alien : aliens) {
                alien.y += 2;
            }

            // Move bullets
            for (Bullet bullet : bullets) {
                bullet.y -= 5;
            }

            // Check for collisions
            checkCollisions();

            // Remove off-screen aliens and bullets
            aliens.removeIf(alien -> alien.y > 600);
            bullets.removeIf(bullet -> bullet.y < 0);

            // Spawn new aliens
            if (aliens.isEmpty()) {
                for (int i = 0; i < 6; i++) {
                    aliens.add(new Alien(i * 100, 0));
                }
            }

            repaint();
        }
    }

    private void checkCollisions() {
        for (Alien alien : new ArrayList<>(aliens)) {
            for (Bullet bullet : new ArrayList<>(bullets)) {
                if (alien.getBounds().intersects(bullet.getBounds())) {
                    aliens.remove(alien);
                    bullets.remove(bullet);
                    score += 10;
                }
            }

            if (alien.getBounds().intersects(new Rectangle(playerX, playerY, 50, 50))) {
                isGameOver = true;
            }
        }
    }

    public void keyTyped(KeyEvent e) {}

    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        if (key == KeyEvent.VK_LEFT && playerX > 0) {
            playerX -= 20;
        }

        if (key == KeyEvent.VK_RIGHT && playerX < 750) {
            playerX += 20;
        }

        if (key == KeyEvent.VK_SPACE) {
            if (!isGameOver) {
                bullets.add(new Bullet(playerX + 20, playerY));
            } else {
                // Restart the game
                isGameOver = false;
                playerX = 300;
                score = 0;
                aliens.clear();
                bullets.clear();
                for (int i = 0; i < 6; i++) {
                    aliens.add(new Alien(i * 100, 0));
                }
            }
        }
    }

    public void keyReleased(KeyEvent e) {}

    public static void main(String[] args) {
        JFrame frame = new JFrame("Space Invaders");
        SpaceInvadersGame game = new SpaceInvadersGame();
        frame.add(game);
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    private class Alien {
        int x, y;

        Alien(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Rectangle getBounds() {
            return new Rectangle(x, y, 50, 50);
        }
    }

    private class Bullet {
        int x, y;

        Bullet(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Rectangle getBounds() {
            return new Rectangle(x, y, 10, 20);
        }
    }
}