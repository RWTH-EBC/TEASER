from teaser.project import Project
import warnings as warnings
import os

prj = Project(False)


class TestModelicaVersions(object):
    """Unit Tests for TEASER"""
    global prj

    def test_modelica_export_version(self):
        try:
            from github import Github
        except ImportError:
            return 0

        from teaser.logic.buildingobjects.calculation.ibpsa import IBPSA
        from teaser.logic.archetypebuildings.bmvbs.office import Office

        prj.set_default()
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500)

        ibpsa = IBPSA(test_office)

        try:
            token = os.environ['GH_Token']
        except:
            token = None
        if token:
            git = Github(login_or_token=token)
        else:
            git = Github()

        try:
            aixlib = git.search_repositories('AixLib')[0].get_tags()[0].name
            print(aixlib.replace('v', ''))
            assert aixlib.replace('v', '') == ibpsa.version['AixLib']
        except IndexError:
            warnings.warn('There was an index error for AixLib', UserWarning)

        try:
            buildings = git.search_repositories(
                'modelica/Buildings')[0].get_tags()[0].name
            assert buildings.replace('v', '') == ibpsa.version['Buildings']
        except IndexError:
            warnings.warn(
                'There was an index error for Buildings', UserWarning)

        try:
            buildingsys = git.search_repositories(
                'UdK-VPT/BuildingSystems')[0].get_tags()[0].name
            assert buildingsys.replace('v', '') == ibpsa.version[
                'BuildingSystems']
        except IndexError:
            warnings.warn('There was an index error for BuildingSys',
                          UserWarning)
        try:
            ideas = git.search_repositories(
                'open-ideas/ideas')[0].get_tags()[0].name
            assert ideas.replace('v', '') == ibpsa.version['IDEAS']
        except IndexError:
            warnings.warn('There was an index error for IDEAS', UserWarning)
