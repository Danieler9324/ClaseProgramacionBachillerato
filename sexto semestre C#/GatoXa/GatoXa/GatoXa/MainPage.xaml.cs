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
        }
        private void ficha(object sender, EventArgs e)
        {
            Button btn = (Button)sender;

            if (btn.Text == "")
            {
                btn.Text = turno;
                cambiar(sender, e);
            }
        }
    }
}
