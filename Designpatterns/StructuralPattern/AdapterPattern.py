# 1. Target interface expected by the client
class IReports:
    def get_json_data(self, data: str) -> str:
        raise NotImplementedError


# 2. Adaptee: provides XML data from raw input
class XmlDataProvider:
    # expects data in "name:id" format (e.g. "Alice:42")
    def get_xml_data(self, data: str) -> str:
        name, user_id = data.split(":")
        return (
            "<user>"
            f"<name>{name}</name>"
            f"<id>{user_id}</id>"
            "</user>"
        )


# 3. Adapter: converts XML output into JSON
class XmlDataProviderAdapter(IReports):
    def __init__(self, xml_provider: XmlDataProvider):
        self.xml_provider = xml_provider

    def get_json_data(self, data: str) -> str:
        # Step 1: Get XML from adaptee
        xml = self.xml_provider.get_xml_data(data)

        # Step 2: Extract values from XML (simple parsing)
        name = xml.split("<name>")[1].split("</name>")[0]
        user_id = xml.split("<id>")[1].split("</id>")[0]

        # Step 3: Convert to JSON format
        return f'{{"name":"{name}", "id":{user_id}}}'


# 4. Client works only with IReports
class Client:
    def get_report(self, report: IReports, raw_data: str):
        print("Processed JSON:", report.get_json_data(raw_data))


# 5. Client code
if __name__ == "__main__":
    xml_provider = XmlDataProvider()
    adapter = XmlDataProviderAdapter(xml_provider)

    raw_data = "Alice:42"

    client = Client()
    client.get_report(adapter, raw_data)
