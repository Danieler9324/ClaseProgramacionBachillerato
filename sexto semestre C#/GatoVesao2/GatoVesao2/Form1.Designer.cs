namespace GatoVesao2
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            b00 = new Button();
            b01 = new Button();
            b02 = new Button();
            b10 = new Button();
            b11 = new Button();
            b12 = new Button();
            b20 = new Button();
            b21 = new Button();
            b22 = new Button();
            label1 = new Label();
            Nombre = new Label();
            Winner = new Label();
            gano = new Label();
            volver = new Button();
            contaX = new Label();
            contaO = new Label();
            contador2 = new Label();
            numericUpDown1 = new NumericUpDown();
            numericUpDown2 = new NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown2).BeginInit();
            SuspendLayout();
            // 
            // b00
            // 
            b00.Font = new Font("Segoe UI", 20F);
            b00.Location = new Point(354, 111);
            b00.Name = "b00";
            b00.Size = new Size(100, 100);
            b00.TabIndex = 0;
            b00.UseVisualStyleBackColor = true;
            b00.Click += b00_Click;
            // 
            // b01
            // 
            b01.Font = new Font("Segoe UI", 20F);
            b01.Location = new Point(473, 111);
            b01.Name = "b01";
            b01.Size = new Size(100, 100);
            b01.TabIndex = 1;
            b01.UseVisualStyleBackColor = true;
            b01.Click += b01_Click;
            // 
            // b02
            // 
            b02.Font = new Font("Segoe UI", 20F);
            b02.Location = new Point(592, 111);
            b02.Name = "b02";
            b02.Size = new Size(100, 100);
            b02.TabIndex = 2;
            b02.UseVisualStyleBackColor = true;
            b02.Click += b02_Click;
            // 
            // b10
            // 
            b10.Font = new Font("Segoe UI", 20F);
            b10.Location = new Point(354, 234);
            b10.Name = "b10";
            b10.Size = new Size(100, 100);
            b10.TabIndex = 3;
            b10.UseVisualStyleBackColor = true;
            b10.Click += b10_Click;
            // 
            // b11
            // 
            b11.Font = new Font("Segoe UI", 20F);
            b11.Location = new Point(473, 234);
            b11.Name = "b11";
            b11.Size = new Size(100, 100);
            b11.TabIndex = 4;
            b11.UseVisualStyleBackColor = true;
            b11.Click += b11_Click;
            // 
            // b12
            // 
            b12.Font = new Font("Segoe UI", 20F);
            b12.Location = new Point(592, 234);
            b12.Name = "b12";
            b12.Size = new Size(100, 100);
            b12.TabIndex = 5;
            b12.UseVisualStyleBackColor = true;
            b12.Click += b12_Click;
            // 
            // b20
            // 
            b20.Font = new Font("Segoe UI", 20F);
            b20.Location = new Point(354, 352);
            b20.Name = "b20";
            b20.Size = new Size(100, 100);
            b20.TabIndex = 6;
            b20.UseVisualStyleBackColor = true;
            b20.Click += b20_Click;
            // 
            // b21
            // 
            b21.Font = new Font("Segoe UI", 20F);
            b21.Location = new Point(473, 352);
            b21.Name = "b21";
            b21.Size = new Size(100, 100);
            b21.TabIndex = 7;
            b21.UseVisualStyleBackColor = true;
            b21.Click += b21_Click;
            // 
            // b22
            // 
            b22.Font = new Font("Segoe UI", 20F);
            b22.Location = new Point(592, 352);
            b22.Name = "b22";
            b22.Size = new Size(100, 100);
            b22.TabIndex = 8;
            b22.UseVisualStyleBackColor = true;
            b22.Click += b22_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(0, 0);
            label1.Name = "label1";
            label1.Size = new Size(50, 20);
            label1.TabIndex = 9;
            label1.Text = "label1";
            // 
            // Nombre
            // 
            Nombre.AutoSize = true;
            Nombre.BackColor = Color.WhiteSmoke;
            Nombre.Font = new Font("Segoe UI", 40F);
            Nombre.Location = new Point(432, 9);
            Nombre.Name = "Nombre";
            Nombre.Size = new Size(180, 89);
            Nombre.TabIndex = 10;
            Nombre.Text = "Gato";
            Nombre.Click += label2_Click;
            // 
            // Winner
            // 
            Winner.AllowDrop = true;
            Winner.AutoSize = true;
            Winner.BackColor = SystemColors.ControlLightLight;
            Winner.Font = new Font("Segoe UI", 20F);
            Winner.Location = new Point(559, 473);
            Winner.Name = "Winner";
            Winner.Size = new Size(0, 46);
            Winner.TabIndex = 11;
            // 
            // gano
            // 
            gano.AutoSize = true;
            gano.BackColor = SystemColors.ButtonHighlight;
            gano.Font = new Font("Segoe UI", 20F);
            gano.Location = new Point(422, 473);
            gano.Name = "gano";
            gano.Size = new Size(99, 46);
            gano.TabIndex = 12;
            gano.Text = "Gano";
            gano.Visible = false;
            gano.Click += label2_Click_1;
            // 
            // volver
            // 
            volver.Enabled = false;
            volver.Location = new Point(710, 473);
            volver.Name = "volver";
            volver.Size = new Size(151, 57);
            volver.TabIndex = 13;
            volver.Text = "Volver a jugar";
            volver.UseVisualStyleBackColor = true;
            volver.Visible = false;
            volver.Click += button1_Click;
            // 
            // contaX
            // 
            contaX.AutoSize = true;
            contaX.BackColor = SystemColors.ButtonShadow;
            contaX.Font = new Font("Segoe UI", 20F);
            contaX.Location = new Point(176, 111);
            contaX.Name = "contaX";
            contaX.Size = new Size(40, 46);
            contaX.TabIndex = 14;
            contaX.Text = "X";
            contaX.Click += label2_Click_2;
            // 
            // contaO
            // 
            contaO.AutoSize = true;
            contaO.BackColor = SystemColors.ButtonShadow;
            contaO.Font = new Font("Segoe UI", 20F);
            contaO.Location = new Point(791, 111);
            contaO.Name = "contaO";
            contaO.Size = new Size(46, 46);
            contaO.TabIndex = 15;
            contaO.Text = "O";
            contaO.Click += label2_Click_3;
            // 
            // contador2
            // 
            contador2.AutoSize = true;
            contador2.Location = new Point(837, 109);
            contador2.Name = "contador2";
            contador2.Size = new Size(50, 20);
            contador2.TabIndex = 16;
            contador2.Text = "label2";
            // 
            // numericUpDown1
            // 
            numericUpDown1.Font = new Font("Segoe UI", 20F);
            numericUpDown1.Increment = new decimal(new int[] { 0, 0, 0, 0 });
            numericUpDown1.InterceptArrowKeys = false;
            numericUpDown1.Location = new Point(222, 111);
            numericUpDown1.Name = "numericUpDown1";
            numericUpDown1.ReadOnly = true;
            numericUpDown1.Size = new Size(75, 52);
            numericUpDown1.TabIndex = 17;
            numericUpDown1.ValueChanged += numericUpDown1_ValueChanged;
            // 
            // numericUpDown2
            // 
            numericUpDown2.Font = new Font("Segoe UI", 20F);
            numericUpDown2.Increment = new decimal(new int[] { 0, 0, 0, 0 });
            numericUpDown2.InterceptArrowKeys = false;
            numericUpDown2.Location = new Point(843, 109);
            numericUpDown2.Name = "numericUpDown2";
            numericUpDown2.ReadOnly = true;
            numericUpDown2.Size = new Size(75, 52);
            numericUpDown2.TabIndex = 18;
            numericUpDown2.ValueChanged += numericUpDown2_ValueChanged;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.ActiveCaptionText;
            ClientSize = new Size(1088, 554);
            Controls.Add(numericUpDown2);
            Controls.Add(numericUpDown1);
            Controls.Add(contador2);
            Controls.Add(contaO);
            Controls.Add(contaX);
            Controls.Add(volver);
            Controls.Add(gano);
            Controls.Add(Winner);
            Controls.Add(Nombre);
            Controls.Add(label1);
            Controls.Add(b22);
            Controls.Add(b21);
            Controls.Add(b20);
            Controls.Add(b12);
            Controls.Add(b11);
            Controls.Add(b10);
            Controls.Add(b02);
            Controls.Add(b01);
            Controls.Add(b00);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).EndInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown2).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button b00;
        private Button b01;
        private Button b02;
        private Button b10;
        private Button b11;
        private Button b12;
        private Button b20;
        private Button b21;
        private Button b22;
        private Label label1;
        private Label Nombre;
        private Label Winner;
        private Label gano;
        private Button volver;
        private Label contaX;
        private Label contaO;
        private Label contador2;
        private NumericUpDown numericUpDown1;
        private NumericUpDown numericUpDown2;
    }
}
