from scrapy.exporters import CsvItemExporter, BaseItemExporter

class SampleExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self.file = file
        super().__init__(**kwargs)

    def export_item(self, item):
        record = str(item).encode('utf=8') + b'\n'
        self.file.write(record)

class CustomCsvItemExporter(CsvItemExporter):
    def __init__(self, file, include_headers_line=True, join_multivalued=',', **kwargs):
        super().__init__(file, include_headers_line, join_multivalued)

    def start_exporting(self):
        self.items = []

    def export_item(self, item):
        print(item)
        self.items.append(item)

    def finish_exporting(self):
        for item in self.items:
            values = [item[x] for x in item]
            self.csv_writer.writerow(values)



