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
                turno = "O";

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
                cambiar(sender, e);
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

        private async Task MostrarGanador(string ganador)
        {
            juegoTerminado = true;
            await DisplayAlert("El juego ha terminado", "El ganador es: " + ganador, "Ok");
            if (ganador == "O")
            {
                contadorO.Text += 1;
            } else
            {
                contadorX.Text += 1;
            }

        }
    }
}