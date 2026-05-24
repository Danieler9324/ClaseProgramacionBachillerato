using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace GatoXa
{
    public partial class MainPage : ContentPage
    {
        string turno = "X";
        bool juegoTerminado = false;

        public MainPage()
        {
            InitializeComponent();
        }

        private void cambiar(object sender, EventArgs e)
        {
            if (turno == "X")
            {
                turno = "O";
            }
            else
            {
                turno = "X";
            }

            lblTurno.Text = "Turno: " + turno;
        }

        private void ficha(object sender, EventArgs e)
        {
            if (juegoTerminado)
            {
                return;
            }
            Button btn = (Button)sender;

            if (btn.Text == null)
            {
                btn.Text = turno;
                verifica_ganador();
                if (!juegoTerminado)
                {
                    cambiar(sender, e);
                }
            }
        }

        private void verifica_ganador()
        {
            string t = turno;
            if (btn00.Text == t && btn01.Text == t && btn02.Text == t) MostrarGanador(t);
            else if (btn10.Text == t && btn11.Text == t && btn12.Text == t) MostrarGanador(t);
            else if (btn20.Text == t && btn21.Text == t && btn22.Text == t) MostrarGanador(t);

            else if (btn02.Text == t && btn11.Text == t && btn20.Text == t) MostrarGanador(t);
            else if (btn00.Text == t && btn11.Text == t && btn22.Text == t) MostrarGanador(t);

            else if (btn00.Text == t && btn10.Text == t && btn20.Text == t) MostrarGanador(t);
            else if (btn01.Text == t && btn11.Text == t && btn21.Text == t) MostrarGanador(t);
            else if (btn02.Text == t && btn12.Text == t && btn22.Text == t) MostrarGanador(t);
        }

        private async void MostrarGanador(string ganador)
        {
            juegoTerminado = true;
            await DisplayAlert("El juego ha terminado", "El ganador es: " + ganador, "Volver a jugar");

            ReiniciarTablero();
        }

        private void ReiniciarTablero()
        {
            btn00.Text = null; btn01.Text = null; btn02.Text = null;
            btn10.Text = null; btn11.Text = null; btn12.Text = null;
            btn20.Text = null; btn21.Text = null; btn22.Text = null;

            juegoTerminado = false;
            turno = "X";
            lblTurno.Text = "Turno: " + turno;
        }
    }
}