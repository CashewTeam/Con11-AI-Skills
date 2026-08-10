# SpatialUIProvider | PICO Spatial SDK

ui:design / com.pico.spatial.ui.design / SpatialUIProvider 
# SpatialUIProvider
```kotlin
class SpatialUIProvider : ContentProvider
```
SpatialUI use Content Provider to access application context 
Members 
## Constructors
Spatial UIProvider 
```kotlin
constructor()
```
## Types
Companion 
```kotlin
object Companion
```
The companion of  SpatialUIProvider . 
## Functions
delete 
```kotlin
open override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int
```get Type 
```kotlin
open override fun getType(uri: Uri): String?
```insert 
```kotlin
open override fun insert(uri: Uri, values: ContentValues?): Uri?
```on Create 
```kotlin
open override fun onCreate(): Boolean
```query 
```kotlin
open override fun query(uri: Uri, projection: Array<out String>?, selection: String?, selectionArgs: Array<out String>?, sortOrder: String?): Cursor?
```update 
```kotlin
open override fun update(uri: Uri, values: ContentValues?, selection: String?, selectionArgs: Array<out String>?): Int
```