import argparse
import csv
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("input_path", help="input path")
parser.add_argument("output_path", help="output path")


DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

def parse_datetime(string):
  return datetime.datetime.strptime(string, DATE_FORMAT)


def main(input_path, output_path):
  with open(input_path) as f:
    reader = csv.DictReader(f)

    tmp = {}
    for row in reader:
      key = (row["Border"], row["Measure"])
      val = (row["Date"], row["Value"])
      if key not in tmp:
        tmp[key] = [val]
      else:
        tmp[key].append(val)

  out = {}
  for group, data in tmp.iteritems():
    count, running_sum = 0, 0
    for val in sorted(data, key=lambda x: parse_datetime(x[0])):
      date, value = val[0], int(val[1])
      key = group + (date,)
      if key not in out:
        avg = int(round(float(running_sum) / count)) if count > 0 else 0
        out[key] = (value, avg)
        count += 1
      else:
        out[key] = (out[key][0] + value, out[key][1])

      running_sum += value

  final = []
  for key, val in out.iteritems():
    final.append({
        "Border": key[0],
        "Measure": key[1],
        "Date": key[2],
        "Value": val[0],
        "Average": val[1],
    })
      
  with open(output_path, "w") as o:
    writer = csv.DictWriter(
        o, fieldnames=["Border", "Date", "Measure", "Value", "Average"])
    writer.writeheader()
    for row in sorted(
        final,
        key=lambda x: (x["Date"], x["Value"], x["Measure"], x["Border"]),
        reverse=True):
      writer.writerow(row)

  return out


if __name__ == "__main__":
  args = parser.parse_args()
  main(args.input_path, args.output_path)
