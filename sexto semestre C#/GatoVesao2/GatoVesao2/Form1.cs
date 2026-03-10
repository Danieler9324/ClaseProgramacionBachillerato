namespace GatoVesao2
{
    public partial class Form1 : Form
    {
        string siguiente = "X";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void termina(string ganador)
        {
            b00.Enabled = false;
            b01.Enabled = false;
            b02.Enabled = false;
            b10.Enabled = false;
            b11.Enabled = false;
            b12.Enabled = false;
            b20.Enabled = false;
            b21.Enabled = false;
            b22.Enabled = false;
            Winner.Text = ganador;
            gano.Visible = true;
            volver.Visible = true;
            volver.Enabled = true;
            if (ganador == "X")
            {
                numericUpDown1.Value += 1;
            }
            if (ganador == "O")
            {
                numericUpDown2.Value += 1;
            }
        }

        private void jugar_de_nuevo()
        {
            b00.Enabled = true;
            b01.Enabled = true;
            b02.Enabled = true;
            b10.Enabled = true;
            b11.Enabled = true;
            b12.Enabled = true;
            b20.Enabled = true;
            b21.Enabled = true;
            b22.Enabled = true;
            b00.Text = "";
            b01.Text = "";
            b02.Text = "";
            b10.Text = "";
            b11.Text = "";
            b12.Text = "";
            b20.Text = "";
            b21.Text = "";
            b22.Text = "";
            Winner.Text = "";
            gano.Visible = false;
            volver.Visible = false;
            volver.Enabled = false;
        }

        private void ver_ganador()
        {
            if (b00.Text != "" && b00.Text == b01.Text && b01.Text == b02.Text)
                termina(b00.Text);

            if (b10.Text != "" && b10.Text == b11.Text && b11.Text == b12.Text)
                termina(b10.Text);

            if (b20.Text != "" && b20.Text == b21.Text && b21.Text == b22.Text)
                termina(b20.Text);

            if (b00.Text != "" && b00.Text == b10.Text && b10.Text == b20.Text)
                termina(b00.Text);

            if (b01.Text != "" && b01.Text == b11.Text && b11.Text == b21.Text)
                termina(b01.Text);

            if (b02.Text != "" && b02.Text == b12.Text && b12.Text == b22.Text)
                termina(b02.Text);

            if (b00.Text != "" && b00.Text == b11.Text && b11.Text == b22.Text)
                termina(b00.Text);

            if (b02.Text != "" && b02.Text == b11.Text && b11.Text == b20.Text)
                termina(b02.Text);

            if (b00.Text != "" && b01.Text != "" && b02.Text != "" &&
                b10.Text != "" && b11.Text != "" && b12.Text != "" &&
                b20.Text != "" && b21.Text != "" && b22.Text != "")
            {
                termina("Empate");
                gano.Visible = false;
            }
        }

        private void cambiar()
        {
            if (siguiente == "X")
            {
                siguiente = "O";
            }
            else
            {
                siguiente = "X";
            }
        }

        private void b00_Click(object sender, EventArgs e)
        {
            if (b00.Text != "") return;
            b00.Text = siguiente;
            cambiar();
            ver_ganador();

        }
        private void b01_Click(object sender, EventArgs e)
        {
            if (b01.Text != "") return;
            b01.Text = siguiente;
            cambiar();
            ver_ganador();

        }
        private void b02_Click(object sender, EventArgs e)
        {
            if (b02.Text != "") return;
            b02.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b10_Click(object sender, EventArgs e)
        {
            if (b10.Text != "") return;
            b10.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b11_Click(object sender, EventArgs e)
        {
            if (b11.Text != "") return;
            b11.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b12_Click(object sender, EventArgs e)
        {
            if (b12.Text != "") return;
            b12.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b20_Click(object sender, EventArgs e)
        {
            if (b20.Text != "") return;
            b20.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b21_Click(object sender, EventArgs e)
        {
            if (b21.Text != "") return;
            b21.Text = siguiente;
            cambiar();
            ver_ganador();
        }
        private void b22_Click(object sender, EventArgs e)
        {
            if (b22.Text != "") return;
            b22.Text = siguiente;
            cambiar();
            ver_ganador();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click_1(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            jugar_de_nuevo();
        }

        private void label2_Click_2(object sender, EventArgs e)
        {

        }

        private void label2_Click_3(object sender, EventArgs e)
        {

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
       
        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }
    }
}