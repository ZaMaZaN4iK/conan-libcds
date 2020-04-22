import os
import shutil
from conans import ConanFile, CMake
from conans import CMake, tools

class CdsConan(ConanFile):
    name = "cds"
    version = "2.3.3"
    archive = "lib%s-%s.tar.gz" % (name, version)
    folder = "lib%s-%s" % (name, version)
    settings = "os", "compiler", "arch", "build_type"
    url = "https://github.com/khizmax/libcds/archive/v%s.tar.gz" % version
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    requires = "boost/1.72.0","gtest/1.8.0@bincrafters/stable"

    def source(self):
        tools.download(self.url, self.archive)
        tools.unzip(self.archive)
        os.unlink(self.archive)

    def build(self):
        root = os.getcwd()
        src_folder = os.path.join(root, self.folder)
        files = os.listdir(src_folder)
        for f in files:
            src_file = os.path.join(src_folder, f)
            dst_file = os.path.join(root, f)
            shutil.move(src_file, dst_file)

        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cds"]
        self.cpp_info.libdirs = ["lib", "lib64"]
