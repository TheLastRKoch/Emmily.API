using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Emily.Business
{
    public class InformationRepository
    {
        public DateTime GetHour ()
        {
            return DateTime.Now;
        }

        public string GetWeather()
        {
            return String.Empty;
        }
    }
}
