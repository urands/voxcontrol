import json
import logging
from pydantic import BaseModel, Field

from fastapi import APIRouter, Request
import spacy

from voxcontrol.models.pretest import (
    extract_form_data,
    find_input_selector_by_label,
    collect_all_labels,
    clean_phone_numbers,
)
from voxcontrol.models.structure import structure, Structure

router = APIRouter(tags=["General route"])
# nlp = spacy.load('ru_core_news_sm')


class RecognitionIn(BaseModel):
    text: str
    sessionId: str | None = Field(default=None)


@router.post("")
async def post_recognition(data: RecognitionIn):
    logging.info(data.sessionId)
    logging.info(data.text)

    # fields = extract_form_data(data.text)
    #
    # logging.info(fields)

    commands = []

    if data.sessionId is not None:
        structure = await Structure.get_or_none(id=data.sessionId)
        text = clean_phone_numbers(data.text)
        labels = collect_all_labels(structure.structure)
        labels = [l.lower().strip() for l in labels]
        logging.info(labels)
        fields = extract_form_data(text, labels)
        logging.info(fields)
        for field, value in fields.items():
            selector = find_input_selector_by_label(structure.structure, field)
            if selector is not None:
                commands.append(
                    {"selector": selector, "value": value, "attribute": "value"}
                )
    return commands

    logging.info(fields)

    # if structure is not None:
    #     logging.info(structure.structure)

    doc = nlp(data.text)
    logging.info(data.text)

    # Выводим сущности
    for ent in doc.ents:
        logging.info(ent.text)
        logging.info(ent.label_)

    return [
        {
            "selector": "html > body > main.container > div.row > div.col-md-12 > form.needs-validation > div.row > div.col-sm-6 input#firstName",
            "attribute": "value",
            "value": data.text,
        }
    ]
