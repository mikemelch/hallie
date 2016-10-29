#!/usr/bin/env python
import speech
import pip
import subprocess


def speakSimilarPackages(similar, package_managers=[], package=None):
    if package_managers and package:
        speech.speak("The package '" + package + "' is not installed with the following package managers:\n" +
                     "\t\t" + "\n\t\t".join(package_managers) + "\n")
    speech.speak("But I found the following similar installed packages:\n" +
                 "\t\t" + "\n\t\t".join(similar) + "\n")


def speakInstalledPackages(package, package_manager, installed, similar=[], speakSimilar=True):
    if installed:
        speech.speak("The package '" + package + "' is installed with the '" + package_manager + "' package manager.\n")
    elif speakSimilar:
        speech.speak("The package '" + package + "' is not installed with the '" + package_manager + "' package manager." +
                     ("" if similar else "\n"))
        if similar:
            speakSimilarPackages(similar)


def checkInstalledPip(package, speak=True, speakSimilar=True):
    """checks if a given package is installed on pip"""
    packages = sorted([i.key for i in pip.get_installed_distributions()])
    installed = package in packages
    similar = None

    if not installed:
        similar = [pkg for pkg in packages if package in pkg]

    if speak:
        speakInstalledPackages(package, "pip", installed, similar, speakSimilar)

    return (installed, similar)


def checkInstalledBrew(package, similar=True, speak=True, speakSimilar=True):
    """checks if a given package is installed on homebrew"""
    packages = subprocess.check_output(['brew', 'list']).split()
    installed = package in packages
    similar = []

    if not installed:
        similar = [pkg for pkg in packages if package in pkg]
    if speak:
        speakInstalledPackages(package, "homebrew", installed, similar, speakSimilar)

    return (installed, similar)


def installPackagePip(package):
    """tries to install a given package on pip"""
    speech.speak("Attempting to install '" + package + "' on the 'pip' package manager.\n")
    pip.main(['install', package])


def installPackageBrew(package):
    """tries to install a given package on homebrew"""
    speech.speak("Attempting to install '" + package + "' on the 'pip' package manager.\n")
    subprocess.check_output(['brew', 'install', package])


def checkInstalled(package, speak=True):
    installedBrew, similarBrew = checkInstalledBrew(package, speak=speak, speakSimilar=False)
    if installedBrew:
        return True

    installedPip, similarPip = checkInstalledPip(package, speak=speak, speakSimilar=False)
    if installedPip:
        return True

    if speak:
        speakSimilarPackages(similarBrew + similarPip, package_managers=["homebrew", "pip"], package=package)

    return False


# TODO: Add more package managers
def installPackage(package):
    """installs a given package from a package manager depending on a user's OS"""
    installPackagePip(package)
