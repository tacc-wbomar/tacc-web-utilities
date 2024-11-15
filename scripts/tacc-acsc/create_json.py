import json
import argparse

# Function to parse the HTML content
def parse_html(html_content, data_type):
    data_list = [
        {
            "pk": 174054,
            "creation_date": "2024-11-13T19:27:54.575Z",
            "position": 0,
            "plugin_type": "Bootstrap4GridRowPlugin",
            "parent_id": None,
            "data": {
                "vertical_alignment": "",
                "horizontal_alignment": "",
                "gutters": False,
                "tag_type": "div",
                "attributes": {}
            }
        }
    ]
    blocks = html_content.split("\n\n<hr>\n\n")
    for i, block in enumerate(blocks):
        lines = block.split("\n")
        if len(lines) < 20:
            continue
        card_text = ''.join(line.strip() for line in lines[:5])
        interview = ''.join(line.strip() for line in lines[8:21])

        entry = [
            {
                "pk": 174200 + i,
                "creation_date": "2024-11-13T19:27:54.575Z",
                "position": i,
                "plugin_type": "Bootstrap4GridColumnPlugin",
                "parent_id": 174054,
                "data": {
                    "column_type": "col",
                    "column_alignment": "",
                    "tag_type": "div",
                    "attributes": {},
                    "xs_col": 12,
                    "xs_order": None,
                    "xs_offset": None,
                    "xs_ml": False,
                    "xs_mr": False,
                    "sm_col": 12,
                    "sm_order": None,
                    "sm_offset": None,
                    "sm_ml": False,
                    "sm_mr": False,
                    "md_col": 12,
                    "md_order": None,
                    "md_offset": None,
                    "md_ml": False,
                    "md_mr": False,
                    "lg_col": 6,
                    "lg_order": None,
                    "lg_offset": None,
                    "lg_ml": False,
                    "lg_mr": False,
                    "xl_col": 6,
                    "xl_order": None,
                    "xl_offset": None,
                    "xl_ml": False,
                    "xl_mr": False
                }
            },
            {
                "pk": 174300 + i,
                "creation_date": "2024-11-13T19:27:54.575Z",
                "position": 0,
                "plugin_type": "StylePlugin",
                "parent_id": 174200 + i,
                "data": {
                    "template": "default",
                    "label": "Card w/ Image",
                    "tag_type": "div",
                    "class_name": "card--image-left",
                    "additional_classes": "card--plain",
                    "id_name": "",
                    "attributes": {},
                    "padding_top": None,
                    "padding_right": None,
                    "padding_bottom": None,
                    "padding_left": None,
                    "margin_top": None,
                    "margin_right": None,
                    "margin_bottom": None,
                    "margin_left": None
                },
            },
            {
                "pk": 174400 + i,
                "creation_date": "2024-11-13T19:27:54.575Z",
                "position": 0,
                "plugin_type": "Bootstrap4PicturePlugin",
                "parent_id": 174300 + i,
                "data": {
                    "template": "default",
                    "picture": 119,
                    "external_picture": None,
                    "width": None,
                    "height": None,
                    "alignment": "",
                    "caption_text": "",
                    "attributes": {},
                    "link_url": None,
                    "link_page": None,
                    "link_target": "",
                    "link_attributes": {},
                    "use_automatic_scaling": True,
                    "use_no_cropping": False,
                    "use_crop": False,
                    "use_upscale": False,
                    "use_responsive_image": "inherit",
                    "thumbnail_options": None,
                    "picture_fluid": True,
                    "picture_rounded": False,
                    "picture_thumbnail": False
                }
            },
            {
                "pk": 174500 + i,
                "creation_date": "2024-11-13T19:27:54.575Z",
                "position": 1,
                "plugin_type": "TextPlugin",
                "parent_id": 174300 + i,
                "data": {
                    "body": card_text
                }
            },
            {
                "pk": 174600 + i,
                "creation_date": "2024-11-13T19:27:54.575Z",
                "position": 1,
                "plugin_type": "TextPlugin",
                "parent_id": 174200 + i,
                "data": {
                    "body": interview
                }
            }
        ]
        data_list.extend(entry)
    return data_list

# Main function to handle file reading and writing
def main(file_name, data_type):
    with open(file_name, 'r') as file:
        html_content = file.read()

    data = parse_html(html_content, data_type)

    output_file = f'{data_type}.json'
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"{output_file} file has been created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process HTML files to JSON.')
    parser.add_argument('type', choices=['participants', 'mentors'], help='Type of data to process')
    args = parser.parse_args()

    file_name = f'{args.type}.html'
    main(file_name, args.type)
