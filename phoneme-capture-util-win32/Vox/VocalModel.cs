using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vox
{
    public class VocalModel
    {
        public VocalModel() { }

        public string[] phonemes = { "AA","AE","AH","AO","AW","AY","B","CH","D","DH","EH","ER","EY","F","G","HH","IH","IY","JH","K","L","M","N","NG","OW","OY","P","R","S","SH","T","TH","UH","UW","V","W","Y","Z","ZH" };
        public string[] tips = { "odd","at","hut","ought","cow","hide","be","cheese","dee","thee","Ed","hurt","ate","fee","green","he","it","eat","gee","key","lee","me","knee","ping","oat","toy","pee","read","sea","she","tea","theta","hood","two","vee","we","yield","zee","seizure" };

        public string name { get; set; }
        public string saveDir { get; set; }
        
    }
}
