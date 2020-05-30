# -*- coding: utf-8 -*-

import json
import logging
import urllib
import werkzeug
import requests

from odoo import _, api, exceptions, fields, http, models, tools
from odoo.http import request
from odoo.http import Response


class SkillAssessment(http.Controller):
    @http.route(['/my/skill-assessment'], type='http', auth="user", website=True)
    def portal_my_skill_assessment(self, **kw):
        partner = request.env.user.partner_id
        values = {}
        r = requests.get('https://test.skill.jobs/api/v1/getStudentResult/'+ str(partner.email))
        skills = json.loads(r.text)
        values.update({
            'skills': skills,
        })
        return request.render("skill_assessment.portal_my_skill_assessment",values)





