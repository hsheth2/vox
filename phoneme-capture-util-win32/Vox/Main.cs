using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

namespace Vox
{
    public partial class Main : Form
    {
        VocalModel voc;
        string teardown_dir;
        int i;
        public Main()
        {
            InitializeComponent();
            voc = new VocalModel();
        }

        private void Main_Load(object sender, EventArgs e)
        {

        }

        [DllImport("winmm.dll", EntryPoint = "mciSendStringA", ExactSpelling = true, CharSet = CharSet.Ansi, SetLastError = true)]
        private static extern int record(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);

        private void btnStart_Click(object sender, EventArgs e)
        {
            i = 0;
            btnSaveDir.Enabled = false;
            btnName.Enabled = false;
            btnStop.Visible = true;
            btnStart.Visible = false;
            btnNext.Visible = true;
            runPrompts();
        }

        private void btnSaveDir_Click(object sender, EventArgs e)
        {
            if (SaveBrowse.ShowDialog() == DialogResult.OK)
            {
                String saveDir = SaveBrowse.SelectedPath;
                voc.saveDir = saveDir;
                lblSaveDir.Text = saveDir;
                if (!String.IsNullOrEmpty(voc.name))
                {
                    btnStart.Enabled = true;
                }
                
            }
            
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            btnStart.Visible = true;
            btnStop.Visible = false;

            MessageBox.Show("Vocal Model Partially Generated.");
            Directory.Delete(teardown_dir, true);
            this.Close();
        }

        private void btnName_Click(object sender, EventArgs e)
        {
            string name = Microsoft.VisualBasic.Interaction.InputBox("Please input a name for this vocal model.", "Name", "", 0, 0);
            if (String.IsNullOrWhiteSpace(name))
            {
                MessageBox.Show("Name not valid.");
            } else
            {
                voc.name = name.Trim();
                lblName.Text = voc.name;
                if (!String.IsNullOrEmpty(voc.saveDir))
                {
                    btnStart.Enabled = true;
                }
            }
        }

        private void runPrompts()
        {
            if (i < voc.phonemes.Length)
            {
                lblPrompt.Text = voc.phonemes[i];
                lblHint.Text = String.Format("Hint: \"{0}\"", voc.tips[i]);
                record("open new Type waveaudio Alias recsound", "", 0, 0);
                record("record recsound", "", 0, 0);
            } else
            {
                MessageBox.Show("Vocal Model Created Successfully!");
                Directory.Delete(teardown_dir, true);
                this.Close();
            }
            
        }

        private void btnNext_Click(object sender, EventArgs e)
        {
            string dir = teardown_dir = voc.saveDir + "\\" + voc.name + "-temp";
            if (!Directory.Exists(dir)) Directory.CreateDirectory(dir);
            string filepath = dir + "\\" + voc.phonemes[i] + ".wav";

            record("save recsound " + filepath, "", 0, 0);
            record("close recsound", "", 0, 0);

            string out_dir = voc.saveDir + "\\" + voc.name;
            if (!Directory.Exists(out_dir)) Directory.CreateDirectory(out_dir);
            Process.Start(@"C:\Program Files (x86)\sox-14-4-2\sox.exe", filepath + " " + out_dir + "\\" + voc.phonemes[i] + @".wav silence 1 0.1 1% -1 0.1 1%");

            i++;
            runPrompts();
        }
    }
}
